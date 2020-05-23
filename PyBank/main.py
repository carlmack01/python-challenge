#
#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#  * The total number of months included in the dataset
#
#  * The net total amount of "Profit/Losses" over the entire period
#
#  * The average of the changes in "Profit/Losses" over the entire period
#
#  * The greatest increase in profits (date and amount) over the entire period
#
#  * The greatest decrease in losses (date and amount) over the entire period
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    months = 0
    total = 0
    value = 867884
    totalchange = 0
    max = 0
    maxdate = ""
    min = 0
    mindate = ""
      # Read each row of data after the header
    csvRows = []
    
    
    
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        #print(row)
        change = int(row[1]) - value
        totalchange = totalchange + change
        months = months + 1
        total = total + int(row[1])
        value = int(row[1])
        if change > max:
            max = change
            maxdate = row[0]
        if change < min:
            min = change
            mindate = row[0]
        
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(months))
print("Total: " + str(total))
print("Average Change: $" + str(totalchange/months))
print("Greatest Increase in Profits: " + str(maxdate) + " $" + str(max))
print("Greatest Decrease in Profits: " + str(mindate) + " $" + str(min))

# Specify the file to write to
output_path = os.path.join("analysis.txt")
os.chdir("analysis")

f=open("analysis.txt", "w+")

f.write("Financial Analysis\n")
f.write("---------------------------\n")
f.write("Total Months: " + str(months) + "\n")
f.write("Total: " + str(total) + "\n")
f.write("Average Change: $" + str(totalchange/months) + "\n")
f.write("Greatest Increase in Profits: " + str(maxdate) + " $" + str(max) + "\n")
f.write("Greatest Decrease in Profits: " + str(mindate) + " $" + str(min) + "\n")


f.close()
