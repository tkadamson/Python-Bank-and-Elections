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

    #Dictionary of candidate and total votes for each
    election = {}

    #Candidate tuple
    candidate_list = ("Correy", "Khan", "Li", "O'Tooley")

    #Vote total list
    votes = [0, 0, 0, 0]

    #Put tuple and list in the dictionary
    election["Candidate"] = candidate_list
    election["Vote Total"] = votes