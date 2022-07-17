# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open (menu_filepath) as menu_csv:
    menu_data = csv.reader(menu_csv, delimiter=",")
    next(menu_data, None)
    
    for row in menu_data:
        menu.append(row)

# Read in the sales data into the sales list
with open (sales_filepath) as sales_csv:
    sales_data = csv.reader(sales_csv, delimiter=",")
    next(sales_data, None)

    for row in sales_data:
        sales.append(row)


# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize constants
COUNT_KEY = "01-count"
REVENUE_KEY= "02-revenue"
COGS_KEY = "03-cogs"
PROFIT_KEY = "04-profit"

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object
for sale in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    qty = int(sale[3])
    menu_item = sale[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    if menu_item not in report:
        report[menu_item] = {
           COUNT_KEY: 0,
           REVENUE_KEY: 0,
           COGS_KEY: 0,
           PROFIT_KEY: 0,
        }
    
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit


    # For every row in our sales data, loop over the menu records to determine a match
    for item in menu:
        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        item_name = item[0]
        price = float(item[3])
        cost = float(item[4])



        # Calculate profit of each item in the menu data
        profit = price - cost


        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if item_name == menu_item:
            # Print out matching menu data
            print(menu_item)
    
            # Cumulatively add up the metrics for each item key
            report[menu_item][COUNT_KEY] += qty
            report[menu_item][REVENUE_KEY] += price * qty
            report[menu_item][COGS_KEY] += cost * qty
            report[menu_item][PROFIT_KEY] += profit * qty

        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f'{menu_item} does not equal {item_name}! NO MATCH!')



    # Increment the row counter by 1
    row_count += 1
 


# Print total number of records in sales data
print(row_count)


report_output = ''

for key in report:
    report_output += f'{key}: \n'
    report_output += f'{COUNT_KEY}: {report[key][COUNT_KEY]}\n'
    report_output += f'{REVENUE_KEY}: {report[key][REVENUE_KEY]}\n'
    report_output += f'{COGS_KEY}: {report[key][COGS_KEY]}\n'
    report_output += f'{PROFIT_KEY}: {report[key][PROFIT_KEY]}\n'
    report_output += '--------------------------------------\n\n'


# Write out report to a text file (won't appear on the command line output)
with open('sales_report.txt', 'w') as report_file:
                  report_file.write(report_output)
      
          
