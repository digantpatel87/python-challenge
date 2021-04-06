import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')
txtfilepath = os.path.join('analysis','finalresult.txt')

#set the counters and default values
Total = 0
CandidateList = []
DistinctCandidateList = []
NumberOfVotes = []
Percentage = []
FinalDist = dict()


with open(csvpath) as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=',')

    #remove header
    header = next(csvreader)

    #loop for each row to count number of months
    for row in csvreader:
        #Number of records counter
        Total = Total + 1
        #Add all records to list
        CandidateList.append(row[2])
    
    #Run throught each 
    for runningData  in set(CandidateList):
        #get Candidate
        DistinctCandidateList.append(runningData)
        #Count number of votes per candidate
        VotesPerCandidate = CandidateList.count(runningData)
        NumberOfVotes.append(VotesPerCandidate)
        # Percentage of votes per candidate
        percentagerCandidate = "{:.3f}".format((VotesPerCandidate/Total)*100)
        Percentage.append(percentagerCandidate)

    MaxNumbersOfVotePerCandidate = max(NumberOfVotes)
    Candidatewinner = DistinctCandidateList[NumberOfVotes.index(MaxNumbersOfVotePerCandidate)]
    
print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {Total}")
print(f"----------------------")
for EachCandidate in range(len(DistinctCandidateList)):
    print(f"{DistinctCandidateList[EachCandidate]}: {Percentage[EachCandidate]}% ({NumberOfVotes[EachCandidate]}) ")
print(f"----------------------")
print(F"The winner is: {Candidatewinner}")
print(f"----------------------")
print(f"```")

outputtxtfile = open(txtfilepath,'w+')
outputtxtfile.write(f"Election Results\n")
outputtxtfile.write(f"----------------------\n")
outputtxtfile.write(f"Total Votes: {Total}\n")
outputtxtfile.write(f"----------------------\n")
for EachCandidate in range(len(DistinctCandidateList)):
    outputtxtfile.write(f"{DistinctCandidateList[EachCandidate]}: {Percentage[EachCandidate]}% ({NumberOfVotes[EachCandidate]})\n")
outputtxtfile.write(f"----------------------\n")
outputtxtfile.write(F"The winner is: {Candidatewinner}\n")
outputtxtfile.write(f"----------------------\n")
outputtxtfile.write(f"```")
