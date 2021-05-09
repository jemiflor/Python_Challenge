# -*- coding: utf-8 -*-
"""
Created on Sat May  8 00:20:00 2021
@author: jemima

Description: Python Challenge Homework - Financial Analysis
"""

# import python csv library
import csv

# declare file path and open the csv file to read
budgetCsvFilePath = 'Resources/budget_data.csv'
with open(budgetCsvFilePath) as budget:
    
    #assign a reader to read the csv file
    reader = csv.reader(budget)
    
    # read the header row
    headerRow = next(reader)
    
    # assign variables to do perform the financial analysis
    totalMonths = 0
    totalRevenue = 0
    totalChange = 0
    averageChange = 0.0
    previousRow = 0
    greatestProfitIncrease = 0
    greatestProfitDecrease = 0
    greatestProfitIncreasePeriod = ''
    greatestProfitDecreasePeriod = ''
    
    # read each row
    for row in reader:
        
        # compute total months - Each row is a month
        totalMonths = totalMonths + 1
        
        #compute total revenue
        totalRevenue = totalRevenue + int(row[1])
        
        #compute the revenue change for each row (month)
        currentRowChange = (int(row[1]) - previousRow)
        
        #if first row assign it to previous row variable - no change
        if (totalMonths == 1):
            previousRow = int(row[1])
        else:
            # not first row. so start aggregating the changes
            totalChange = totalChange + currentRowChange
            # assign current row to previous row for computing current change and aggregating it
            previousRow = int(row[1])
        
            
        # compare change to previous change and swap if current change is high then update 
        # previous high with current change and capture the period        
        if (currentRowChange > 0) and (currentRowChange > greatestProfitIncrease):
            greatestProfitIncrease = currentRowChange
            greatestProfitIncreasePeriod = row[0]
        
        # compare change to previous change and swap if current change is small then update
        # previous low with current change and capture the period
        if (currentRowChange < 0) and (currentRowChange < greatestProfitDecrease):
            greatestProfitDecrease = currentRowChange
            greatestProfitDecreasePeriod = row[0]
            
    # compute average change
    averageChange = totalChange/(totalMonths - 1)
    
    # print to console for debug.
    print ("Financial Analysis")
    print ("------------------------------------------")
    print (f"Total Months: {totalMonths}")
    print (f"Total: ${totalRevenue}")
    print (f"Average Change: ${averageChange}")
    print (f"Greatest Increase In Profit: {greatestProfitIncreasePeriod} (${greatestProfitIncrease})")
    print (f"Greatest Decrease In Profit: {greatestProfitDecreasePeriod} (${greatestProfitDecrease})")
    
    # write results to a file
    with open('Analysis/FinancialAnalysis.txt', 'w') as resultsFile:
        resultsFile.write ("Financial Analysis\n")
        resultsFile.write("---------------------------------------\n")
        resultsFile.write (f"Total Months: {totalMonths}\n")
        resultsFile.write (f"Total: ${totalRevenue}\n")
        resultsFile.write (f"Average Change: ${averageChange}\n")
        resultsFile.write (f"Greatest Increase In Profit: {greatestProfitIncreasePeriod} (${greatestProfitIncrease})\n")
        resultsFile.write (f"Greatest Decrease In Profit: {greatestProfitDecreasePeriod} (${greatestProfitDecrease})\n")
    
    
    
    