# -*- coding: utf-8 -*-
"""
Created on Sat May  8 00:20:00 2021
@author: jemima

Description: Python Challenge Homework - PyPoll - Election Results
"""

# import python csv module
import csv

# declare file path and open the csv file to read
pollDataFilePath = 'Resources/election_data.csv'
with open(pollDataFilePath) as pollData:
    
    #assign a reader to read the csv file
    reader = csv.reader(pollData)
    
    # read the header row
    headerRow = next(reader)
    
    candidates = {}
    totalVotes = 0
    tempHighestPopularVotes = 0
    popularVoteWinner = ""
    
    for row in reader:
 
        totalVotes = totalVotes + 1
        
        if (row[2] in candidates.keys()) :
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
            
    print ("Election Results")
    print ("--------------------------------")
    print (f"Total Votes: {totalVotes}")   
    print ("--------------------------------")     
    for candidate in candidates:
        candidateVotes = candidates[candidate]
        percentageWon = "{:.3f}".format(candidateVotes * 100 / totalVotes)
        print(f"{candidate}: {percentageWon}% ({candidateVotes})")
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