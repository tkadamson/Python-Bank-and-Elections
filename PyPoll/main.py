# Import modules to read/write csv's
import os
import csv

# Get file path to read
pypoll = os.path.join('Resources', 'election_data1.csv')

#Initialize csv reader
with open(pypoll, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # get past header
    csvHeader = next(csvreader)

    #Summation variable
    voteSum = 0

    #Dictionary of candidate and total votes for each
    election = {}

    #Candidate tuple
    candidate_list = ("Correy", "Khan", "Li", "O'Tooley")

    #Vote total list
    votes = [0, 0, 0, 0]
    votePerecnt = []

    #Put tuple and list in the dictionary
    election["Candidate"] = candidate_list
    election["Vote Total"] = votes
    election["Percent"] = votePerecnt

    #Loop through all rows
    for row in csvreader:

        voteSum = voteSum + 1

        #Conditional adding to the vote total a for each time the candidate occurs in the csv
        if row[2] == election["Candidate"][0]:
            election["Vote Total"][0] = election["Vote Total"][0] + 1
        
        if row[2] == election["Candidate"][1]:
            election["Vote Total"][1] = election["Vote Total"][1] + 1

        if row[2] == election["Candidate"][2]:
            election["Vote Total"][2] = election["Vote Total"][2] + 1
        
        if row[2] == election["Candidate"][3]:
            election["Vote Total"][3] = election["Vote Total"][3] + 1
    
#Percent changes

for i in range(4):

    voteShare = round((election["Vote Total"][i]/voteSum) * 100, 2)

    #Append to Percent in dictionary
    election["Percent"].append(voteShare)

#Determine winner
