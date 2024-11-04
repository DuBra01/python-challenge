"""PyBank Homework Starter File"""

import csv
import os

# Define file paths
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

# Read the CSV file
with open(file_to_load, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Track the date and profit/loss
        dates.append(date)
        net_total += profit_loss
        total_months += 1

        # Calculate the monthly change if previous month exists
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        # Update previous profit/loss for next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare results in terminal format
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Profit/Losses: ${net_total}\n"
    f"Average Change in Profit/Losses: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print results to terminal
print(output)

# Write results to text file
with open(file_to_output, 'w') as output_file:
    output_file.write(output)