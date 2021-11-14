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
        if thisCandidate !in candidateDict.keys()

    analysisInfo = ('
        ')
    print(analysisInfo)
    #file_object.write(analysisInfo)
    file_object.close()
