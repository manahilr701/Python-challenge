import csv
from pathlib import Path

# Define the file path
file_path = Path("PyBank/Resources/budget_data.csv")

# Function to check if a value is an integer
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
months = []

# Open and read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        if len(row) != 2:  # Check if the row has exactly 2 columns
            continue
        
        date = row[0]
        profit_loss = row[1]
        
        # Check if profit_loss is a valid integer
        if is_integer(profit_loss):
            profit_loss = int(profit_loss)
            
            # Calculate the total number of months
            total_months += 1
            # Calculate the net total amount of "Profit/Losses"
            total_profit_losses += profit_loss
            
            # Calculate the changes in "Profit/Losses"
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                months.append(date)
            
            # Update the previous profit/loss value
            previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Calculate the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease_month = months[changes.index(greatest_decrease)]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_path = Path("/Users/manahilrashid/Downloads/challenge 3/PyBank/Resources/financial_analysis.txt")
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
