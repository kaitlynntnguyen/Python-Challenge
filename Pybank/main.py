import os
import csv

csvpath=os.path.join("pybank","resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # total months
    next(csvreader)
    data = list(csvreader)
    total_months = len(data)

  # total
    total = 0
    for i in range(0, total_months): 
        total = total + int(data[i][1]) 

  # average change
    p1 = 0
    p2 = int(data[0][1])
    change = 0
    profits = list()
    for j in range(1, total_months):
        p1 = int(data[j][1])
        change = p1 - p2
        profits.append(change)
        p2 = int(data[j][1])
    avgChange = round(sum(profits)/len(profits),2)

  # greatest increase 
    greatest_increase = max(profits)
    greatest_increase_month = profits.index(greatest_increase)+1
    
  # greatest decrease
    greatest_decrease = min(profits)
    greatest_decrease_month = profits.index(greatest_decrease)+1

##### EXPECTED RESULT #####
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

#  print results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avgChange:,}")
    print(f"Greatest Increase in Profits: {data[greatest_increase_month][0]} (${greatest_increase:,})")
    print(f"Greatest Decrease in Profits: {data[greatest_decrease_month][0]} (${greatest_decrease:,})")

    # print to file
    print("Financial Analysis", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Total Months: {total_months:,}", file=open("PyBank.txt", "a"))
    print(f"Average Change: ${avgChange:,}", file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Profits: {data[greatest_increase_month][0]} (${greatest_increase:,})", file=open("PyBank.txt", "a"))
    print(f"Greatest Decrease in Profits: {data[greatest_decrease_month][0]} (${greatest_decrease:,}", file=open("PyBank.txt", "a"))