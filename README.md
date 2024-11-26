# Dynamic CSV Expense Tracker

A Python-based graphical application that allows users to analyze expenses from any CSV file dynamically. Users can load a CSV file, select relevant columns for categorization and amounts, and visualize the data in a bar chart.

---

## Features

- **Dynamic Column Selection:** Supports any CSV file by allowing users to select columns for analysis.
- **Interactive Visualization:** Displays expenses by category in a visually appealing bar chart.
- **Total Expense Calculation:** Calculates and displays the total amount spent.
- **Modern GUI:** User-friendly interface built with Tkinter.
- **File Selection Dialog:** Users can easily select their CSV files using a file dialog.

---

## Requirements

To run the application, make sure you have the following installed:

- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `tkinter` (built-in with Python)

---


Instructions for Usage:
Prepare Your Data:

The application requires a CSV file containing your monthly expenses. Make sure your CSV file is structured in the following format:
Date	Description	Amount	Category
2024-11-01	Groceries	120.50	Food
2024-11-02	Rent	1500.00	Housing
2024-11-03	Electricity Bill	60.00	Utilities
2024-11-04	Water Bill	35.00	Utilities
2024-11-05	Internet	45.00	Utilities
Save the data as expanded_monthly_expenses.csv or modify the file path in the script to match your dataset location.

Running the Application:

After preparing your data, save the Python script and the CSV file in the same folder.
Run the Python script:
python expense_tracker.py
Using the GUI:

When the application window opens, click the "Load Expenses and Show Chart" button.
The total expenses will be displayed at the top.
A bar chart will appear below showing how expenses are distributed across different categories.

Interacting with the Application:

The button will load the data from the CSV file and display:
The total expenses for the month.
A bar chart showing the expenses distribution by category.
The bar chart will update each time you click the button, providing a fresh visualization based on the data.
