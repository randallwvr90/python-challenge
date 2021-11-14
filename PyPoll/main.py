import csv
import os

# set the relative file path 
csvpath = os.path.join('Resources','election_data.csv')

file_object = open('analysis.txt','w')

totalVotes = 0 # an accumulator
candidateList = []
candidateDict = {}

# read election_data.csv
with open(csvpath) as electionData:
    # make a csv reader object
    csvReader = csv.reader(electionData)

    # read the header
    csvHeader = next(csvReader)
    #print(f'CSV header: {csvHeader}')

    # read the rest of the data
    for r in csvReader:
        thisID = r[0]
        thisCounty = r[1]
        thisCandidate = r[2]

        totalVotes += 1
        if thisCandidate in candidateDict:
            candidateDict[thisCandidate] +=1
        else:
            candidateDict[thisCandidate] = 1

    # make a string named analysisInfo presenting the important information. Print the string to the terminal. 
    voteTotalInfo = 'The total number of votes cast was: ' + str(totalVotes) + '.'

    candidateInfo = ''
    for candidate in candidateDict:
        pct = round(candidateDict[candidate] / totalVotes * 100)
        infoStr = f'{candidate} recieved {pct}%, with {candidateDict[candidate]} votes.\n'
        candidateInfo = candidateInfo +infoStr 

    max_key = max(candidateDict, key=candidateDict.get)
    winnerInfo = f'Winner: {max_key}'
    analysisInfo = (voteTotalInfo + '\n'
        + candidateInfo + winnerInfo)
    print(analysisInfo)

    # write to the text file
    file_object.write(analysisInfo)
    file_object.close()
