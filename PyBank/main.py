# Import modules to read/write csv's
import os
import csv

# Get file path
pybank = os.path.join('Resources', 'budget_data1.csv')

with open(pybank, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # get past header
    csvHeader = next(csvreader)

    # initiate for loop for whole csv
    for row in csvreader:
        