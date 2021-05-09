# Python_Challenge
This was an excellent assignment to use the basic concepts of python that we had learnt. 
Used variables, if statements, for loops, dictionaries, iterated dictionary, csv libraries and file read write functions to implement the assignment, PyBank and PyPoll

**PyBank Script**
```
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
```

PyPoll Script
```
# import python csv module
import csv

# declare file path and open the csv file to read
pollDataFilePath = 'Resources/election_data.csv'
with open(pollDataFilePath) as pollData:
    
    #assign a reader to read the csv file
    reader = csv.reader(pollData)
    
    # read the header row
    headerRow = next(reader)
    
    #declare variables to compute total votes, and temporary 
    #popular votes to find popular votes winner
    candidates = {} # Candidate dictionary - Empty at first
    totalVotes = 0
    tempHighestPopularVotes = 0 # initalize highest popular vote count
    popularVoteWinner = "" # temporarily set to empty
    
    # read election data file row by row
    for row in reader:
 
        #each row is one vote - aggregate to find total votes
        totalVotes = totalVotes + 1
        
        #if candidate already added to dictionary then increment
        # candidate vote count
        if (row[2] in candidates.keys()) :
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            # new candidate - add to dictionary and initialize vote count
            candidates[row[2]] = 1
            
    print ("Election Results")
    print ("--------------------------------")
    print (f"Total Votes: {totalVotes}")   
    print ("--------------------------------")   
    
    #loop through all the candidates in the dictionary
    for candidate in candidates:
        
        # get candidate votes
        candidateVotes = candidates[candidate]
        
        # Compute candidate win percentage
        percentageWon = "{:.3f}".format(candidateVotes * 100 / totalVotes)
        print(f"{candidate}: {percentageWon}% ({candidateVotes})")
        
        # Check if candidate vote against temp variable and 
        # if greater than temp then update temp count with candidate count
        # and candidate name
        if (candidateVotes > tempHighestPopularVotes):
            popularVoteWinner = candidate
            tempHighestPopularVotes = candidateVotes
    print ("--------------------------------")  
    print (f"Winner: {popularVoteWinner}")
    print ("--------------------------------")  
    
    
     # write results to a file
    with open('Analysis/ElectionResults.txt', 'w') as resultsFile:
        resultsFile.write ("Election Results\n")
        resultsFile.write ("--------------------------------\n")
        resultsFile.write (f"Total Votes: {totalVotes}\n")   
        resultsFile.write ("--------------------------------\n")     
        for candidate in candidates:
            candidateVotes = candidates[candidate]
            percentageWon = "{:.3f}".format(candidateVotes * 100 / totalVotes)
            resultsFile.write(f"{candidate}: {percentageWon}% ({candidateVotes})\n")
            if (candidateVotes > tempHighestPopularVotes):
                popularVoteWinner = candidate
                tempHighestPopularVotes = candidateVotes
        resultsFile.write ("--------------------------------\n")  
        resultsFile.write (f"Winner: {popularVoteWinner}\n")
        resultsFile.write ("--------------------------------\n")  
```
