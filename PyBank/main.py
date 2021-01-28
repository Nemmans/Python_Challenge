# Import modules
import os
import csv

# Define variables
total_months = 0
net_profit_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set path to file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open & read CSV file
with open(csvpath, newline='') as csvfile:
    
    # Create Csv reader
    budget_data = csv.reader(csvfile, delimiter=',')
    
    # Read header, skip if no header
    csv_header = next(budget_data)
    row = next(budget_data)
    
    # Calculate # of months, net "Profit/Losses" & set variables for rows
    previous_row = int(row[1])
    total_months += 1
    net_profit_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read rows of data after the header | # Thanks Sharon Templin
    for row in budget_data:
        
        # Calculate total number of months included in dataset
        total_months += 1
        
        # Calculate net amount of "Profit/Losses" over the entire period
        net_profit_amount += int(row[1])

        # Calculate % change month to previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate the greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate the average & the date
    average_change = sum(monthly_change)/ len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print analysis | #Stack Overflow
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify File To Write To
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

# Write New Data | Thanks StackOverflow
txtfile.write(f"Financial Analysis\n")
txtfile.write(f"---------------------------\n")
txtfile.write(f"Total Months: {total_months}\n")
txtfile.write(f"Total: ${net_profit_amount}\n")
txtfile.write(f"Average Change: ${average_change}\n")
txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
