# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Define file path
file_path = os.path.join("/Users/lauramitchellemagallanes/Downloads/python-challenge/PyBank/Resources","budget_data.csv")

# Define output file path
file_to_output = os.path.join("/Users/lauramitchellemagallanes/Downloads/python-challenge/PyBank/analysis", "financial_analysis.txt")

# Define variables to track the financial data
total_months = 0
total_net = 0
differences = []
dates = []

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    # Process each row of data
    previous_profit = int(next(csv_reader)[1])  
    total_months = 1
    total_net = previous_profit

    for row in csv_reader:
        # Track the total number of months
        total_months += 1

        # Track the total net amount (sum of profit/loss)
        total_net += int(row[1])

        # Track changes in profit/loss for calculating average change
        change = int(row[1]) - previous_profit
        differences.append(change)
        dates.append(row[0])  # Store the date of the change

        # Update the previous month's profit/loss
        previous_profit = int(row[1])

# Calculate average change
average_change = sum(differences) / len(differences) if differences else 0

# Find greatest increase and decrease in profits
greatest_increase = max(differences) if differences else 0
greatest_decrease = min(differences) if differences else 0

# Find the dates for greatest increase and decrease 
greatest_increase_date = dates[differences.index(greatest_increase)] if differences else ""
greatest_decrease_date = dates[differences.index(greatest_decrease)] if differences else ""

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
