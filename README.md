# expenses___
The provided Python script is a streamlined, educational Expense Tracker designed to demonstrate core programming concepts without relying on external libraries such as json, csv, or pandas. By strictly utilizing Python's built-in capabilities, the code offers a transparent view of how data management, file I/O, and user interacting
Simple Python Expense Tracker

Overview of the Project

This is a lightweight, beginner-friendly Expense Tracker application built entirely in Python.

The unique feature of this project is that it uses zero external libraries (not even standard imports like json or os). It demonstrates how to build a functional application using only core Python concepts:

Manual file handling (reading/writing text files).

String manipulation (splitting and formatting).

Input validation and error handling.

Command-line interface (CLI) loops.

It is designed to help users track their daily spending easily while keeping the code simple and transparent.

Features

Add New Expenses: Record details including Date, Category, Description, and Amount.

View Expenses: Display a clean, formatted text table of all recorded transactions.

Total Calculation: Automatically calculates and shows the total sum of money spent.

Data Persistence: Saves all data to a local text file (expenses.txt) so your records are not lost when you close the program.

Input Validation: Prevents the program from crashing if a user enters text instead of a number for the cost.

Technologies/Tools Used

Language: Python 3.x

Libraries: None (Pure Python)

Storage: Plain Text File (.txt)

Interface: Command Line Interface (CLI) / Terminal

Steps to Install & Run the Project

Install Python:
Ensure you have Python installed on your computer. You can download it from python.org.

Download the Code:
Save the project code into a file named expense_tracker.py.

Open Terminal/Command Prompt:
Navigate to the folder where you saved the file.

Run the Application:
Type the following command and press Enter:

python expense_tracker.py


Instructions for Testing

To ensure the application is working correctly, follow these steps:

Start the App: Run the script. You should see the Main Menu.

Test Adding Data:

Select Option 1 (Add Expense).

Enter a date (e.g., 2023-10-27).

Enter a description (e.g., Coffee).

Enter an amount (e.g., 5.50).

Enter a category (e.g., Food).

Test Viewing Data:

Select Option 2.

Verify that the "Coffee" entry appears in the table.

Check that the "Total Spent" calculates correctly.

Test Persistence:

Select Option 3 to Exit.

Run the script again (python expense_tracker.py).

Select Option 2 immediately. Your previous entry should still be there!

Screenshots (Terminal Output)

1. Main Menu

=== EXPENSE TRACKER (No Libraries) ===
1. Add Expense
2. View Expenses
3. Exit
Enter choice: 


2. Viewing Expenses Table

--- Your Expenses ---
Date         | Category        | Description          | Amount
-----------------------------------------------------------------
2023-11-01   | Food            | Lunch Sandwich       | $12.50
2023-11-02   | Transport       | Bus Ticket           | $2.75
-----------------------------------------------------------------
Total Spent: $15.25




<img width="855" height="795" alt="image" src="https://github.com/user-attachments/assets/031d9582-d273-4c31-8391-09b7af8b82e1" />

