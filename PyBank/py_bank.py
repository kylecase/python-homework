# Initialize imports, variables, and constants
import csv

DATE_COLUMN = 0
PNL_COLUMN = 1

total_months = 0
total = 0
average_change = 0
greatest_increase = ['', '0']
greatest_decrease = ['', '0']


# Read data from csv
with open ('./Resources/budget_data.csv') as csv_file:
    budget = csv.reader(csv_file, delimiter=",")
    next(budget, None)
    
    # iterate through csv file
    for row in budget:
        month_pnl = int(row[PNL_COLUMN])
        # increment month count
        total_months += 1
        
        # add current month to total
        total += month_pnl
        
        # find greatest increase
        if int(greatest_increase[PNL_COLUMN]) == 0:
            greatest_increase = row
        elif month_pnl > int(greatest_increase[PNL_COLUMN]):
            greatest_increase = row
        
        # find greatest decrease
        if int(greatest_decrease[PNL_COLUMN]) == 0:
            greatest_decrease = row
        elif month_pnl < int(greatest_decrease[PNL_COLUMN]):
            greatest_decrease = row
        
# calculate the average
average_change = round(total / total_months, 2)

# helper function for printing a summary string
def generate_summary():
    return "Financial Analysis \n----------------------------\n" + f"Total Months: {total_months}\nTotal: ${total}\nAverage  Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase[DATE_COLUMN]} (${greatest_increase[PNL_COLUMN]})\nGreatest Decrease in Profits: {greatest_decrease[DATE_COLUMN]} (${greatest_decrease[PNL_COLUMN]})"

# Print summary
print(generate_summary())

# Write summary to txt file
with open('summary.txt', 'w') as file:
    file.write(generate_summary())