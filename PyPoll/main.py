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