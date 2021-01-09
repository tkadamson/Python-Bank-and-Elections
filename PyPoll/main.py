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

    #Dictionary of candidates and total votes for each
    election = {}

    #Candidate tuple
    candidate_list = ("Correy", "Khan", "Li", "O'Tooley")

    #Vote total list and vote percentage
    votes = [0, 0, 0, 0]
    votePerecnt = []

    #Put tuple and list in the dictionary
    election["Candidate"] = candidate_list
    election["Vote Total"] = votes
    election["Percent"] = votePerecnt

    #Loop through all rows and read in totals to Vote Total list
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
highestVote = 0

for i in range(4):

    if election["Vote Total"][i] > highestVote:

        highestVote = election["Vote Total"][i]
        winner = election["Candidate"][i]

#Initialize csv witer

# Get file path to write
outputPath = os.path.join('Resources', 'analysis.txt')

# Initialize csv writer
with open(outputPath, 'w') as txtfile:

    #Print analysis to both the terminal and the text file
    txtfile.write("Election Results\n")
    print("Election Results")

    txtfile.write("-------------------------\n")
    print("-------------------------")

    txtfile.write(f"Total Votes: {voteSum}\n")
    print(f"Total Votes: {voteSum}")

    txtfile.write("-------------------------\n")
    print("-------------------------")

    txtfile.write(f'{election["Candidate"][0]}: {election["Percent"][0]}% ({election["Vote Total"][0]})\n')
    print(f'{election["Candidate"][0]}: {election["Percent"][0]}% ({election["Vote Total"][0]})')

    txtfile.write(f'{election["Candidate"][1]}: {election["Percent"][1]}% ({election["Vote Total"][1]})\n')
    print(f'{election["Candidate"][1]}: {election["Percent"][1]}% ({election["Vote Total"][1]})')

    txtfile.write(f'{election["Candidate"][2]}: {election["Percent"][2]}% ({election["Vote Total"][2]})\n')
    print(f'{election["Candidate"][2]}: {election["Percent"][2]}% ({election["Vote Total"][2]})')

    txtfile.write(f'{election["Candidate"][3]}: {election["Percent"][3]}% ({election["Vote Total"][3]})\n')
    print(f'{election["Candidate"][3]}: {election["Percent"][3]}% ({election["Vote Total"][3]})')

    txtfile.write("-------------------------\n")
    print("-------------------------")

    txtfile.write(f"Winner: {winner}\n")
    print(f"Winner: {winner}")