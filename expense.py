import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Global variable to hold the loaded DataFrame
dataframe = None


# Load the CSV file
def load_csv_file():
    global dataframe
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    if not file_path:
        return

    try:
        dataframe = pd.read_csv(file_path)
        column_selector_window()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")


# Open a window for column selection
def column_selector_window():
    global dataframe
    if dataframe is None:
        messagebox.showerror("Error", "No data loaded.")
        return

    # New window for column selection
    column_window = tk.Toplevel(root)
    column_window.title("Select Columns")
    column_window.geometry("400x300")
    column_window.config(bg="#f4f4f9")

    tk.Label(column_window, text="Select Category Column:", bg="#f4f4f9").pack(pady=5)
    category_var = tk.StringVar(column_window)
    category_dropdown = ttk.Combobox(column_window, textvariable=category_var, values=list(dataframe.columns))
    category_dropdown.pack(pady=10)

    tk.Label(column_window, text="Select Amount Column:", bg="#f4f4f9").pack(pady=5)
    amount_var = tk.StringVar(column_window)
    amount_dropdown = ttk.Combobox(column_window, textvariable=amount_var, values=list(dataframe.columns))
    amount_dropdown.pack(pady=10)

    def confirm_selection():
        category_col = category_var.get()
        amount_col = amount_var.get()
        if not category_col or not amount_col:
            messagebox.showerror("Error", "Both columns must be selected.")
            return
        process_data(category_col, amount_col)
        column_window.destroy()

    tk.Button(column_window, text="Confirm", command=confirm_selection, bg="#4A90E2", fg="white").pack(pady=20)


# Process data based on selected columns
def process_data(category_col, amount_col):
    global dataframe
    try:
        total_expenses = dataframe[amount_col].sum()
        category_expenses = dataframe.groupby(category_col)[amount_col].sum()

        # Update GUI
        label_total_expenses.config(text=f"Total Expenses: ${total_expenses:,.2f}")
        show_bar_chart(category_expenses)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process data: {e}")


# Display bar chart
def show_bar_chart(category_expenses):
    # Clear the existing chart, if any
    for widget in frame_chart.winfo_children():
        widget.destroy()

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    category_expenses.plot(kind="bar", ax=ax, color="cadetblue")

    # Add labels and title
    ax.set_xlabel("Category", fontsize=12, fontweight="bold")
    ax.set_ylabel("Amount Spent", fontsize=12, fontweight="bold")
    ax.set_title("Expense Distribution by Category", fontsize=16, fontweight="bold")
    ax.tick_params(axis="x", rotation=45, labelsize=10)

    # Embed plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# Create the main GUI window
root = tk.Tk()
root.title("Dynamic CSV Expense Tracker")
root.geometry("850x700")
root.config(bg="#f4f4f9")

# Frame for title and buttons
frame_top = tk.Frame(root, bg="#f4f4f9")
frame_top.pack(pady=20, padx=30, fill=tk.X)

# Title Label
title_label = tk.Label(
    frame_top,
    text="CSV Expense Tracker",
    font=("Helvetica", 24, "bold"),
    bg="#f4f4f9",
    fg="#333333",
)
title_label.grid(row=0, column=0, pady=10, sticky="w")

# Total Expenses Label
label_total_expenses = tk.Label(
    frame_top,
    text="Total Expenses: $0.00",
    font=("Helvetica", 16),
    bg="#f4f4f9",
    fg="#333333",
)
label_total_expenses.grid(row=1, column=0, pady=10, sticky="w")

# Load CSV Button
def on_enter(e):
    button_load_data.config(bg="#5A9EFC")


def on_leave(e):
    button_load_data.config(bg="#4A90E2")


button_load_data = tk.Button(
    frame_top,
    text="Load CSV File",
    font=("Helvetica", 14),
    bg="#4A90E2",
    fg="white",
    command=load_csv_file,
    relief="flat",
)
button_load_data.grid(row=2, column=0, pady=15, sticky="w")
button_load_data.bind("<Enter>", on_enter)
button_load_data.bind("<Leave>", on_leave)

# Frame for chart
frame_chart = tk.Frame(root, bg="#f4f4f9")
frame_chart.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

# Run the application
root.mainloop()
