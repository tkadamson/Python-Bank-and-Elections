# Import modules to read/write csv's
import os
import csv

# Get file path
pybank = os.path.join('Resources', 'budget_data1.csv')

with open(pybank, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # get past header
    csvHeader = next(csvreader)

    #Variable declarations
    months = 0
    total = 0
    greatestIncrease = 0
    greatestDecrease = 0
    previousDayTotal = 0
    change = []

    # initiate for loop for whole csv
    for row in csvreader:
        # Add to months
        months = months + 1

        # Add to running total
        total = total + int(row[1])

        #Calculate change from previous day and add to change list
        currentChange = int(row[1]) - previousDayTotal

        change.append(currentChange)

        #Greatest Increase Check
        if currentChange > greatestIncrease:
            greatestIncrease = currentChange

            greatestIncMonth = str(row[0])
        
        # Greatest decrease check
        if currentChange < greatestDecrease:
            greatestDecrease = currentChange

            greatestDecMonth = str(row[0])

        # Set today's total as previous day total before the next loop
        previousDayTotal = int(row[1])
        
    print(total)
    print(months)
    print(greatestIncMonth)
    print(greatestIncrease)
    print(greatestDecMonth)
    print(greatestDecrease)

        