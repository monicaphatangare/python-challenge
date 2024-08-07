import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
print (csvpath)
with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvReader)
    
    total_months = 1
    prev_profit = int(next(csvReader)[1])
    net_profit = prev_profit
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    for row in csvReader:
          #print(row[0])
          # The total number of months included in the dataset
          total_months = total_months + 1

          # The net total amount of "Profit/Losses" over the entire period
          net_profit = net_profit + int(row[1])

          # The changes in "Profit/Losses" over the entire period 
          change = int(row[1]) - prev_profit
          prev_profit = int(row[1])
          total_change = total_change + change
          
          # The greatest increase in profits (date and amount) over the entire period
          if change > greatest_increase:
               greatest_increase = change
               greatest_increase_date = row[0]

               # The greatest decrease in profits (date and amount) over the entire period
          if change < greatest_decrease:
               greatest_decrease = change
               greatest_decrease_date = row[0]             

     # The average of those changes
    average = (total_change) / (total_months -1 )

    print(" Financial Analysis")
    print("----------------------------------------")    
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})")


csvpath = os.path.join('..','analysis','Financial_Analysis_Output.txt')
with open(csvpath,"w") as file:
     print(csvpath)
# Write methods to print to Financial_Analysis_Output 
     file.write(f"Financial Analysis \n")
     file.write("---------------------------------------- \n")    
     file.write(f"Total Months:{total_months} \n")
     file.write(f"Total: ${net_profit}\n")
     file.write(f"Average Change: ${average} \n")
     file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n")
     file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease}) \n")
