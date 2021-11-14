import csv
import os

# set the relative file path 
csvpath = os.path.join('Resources','budget_data.csv')
#print(csvpath)

totalMonths = 0 # an accumulator
totalProfit = 0 # an accumulator

totalProfitChange = 0 # an accumulator

greatestIncrease = 0 # not rigorous - assumes positive profits occurred. 
greatestIncreaseDate = ''

greatestDecrease = 0 # not rigorous - assumes negative profits occurred. 
greatestDecreaseDate = ''

file_object = open('analysis.txt','w')

# read budget_data.csv
with open(csvpath) as budgetData:
    # make a csv reader object
    csvReader = csv.reader(budgetData)

    # read the header
    csvHeader = next(csvReader)
    #print(f'CSV header: {csvHeader}')

    # read the rest of the data and count the number of months
    for r in csvReader:
        thisDate = r[0]
        thisProfit = int(r[1])

        totalMonths += 1
        totalProfit += thisProfit

        # add the current profit to the runing total
        totalProfitChange += thisProfit

        if thisProfit > greatestIncrease:
            greatestIncrease = thisProfit
            greatestIncreaseDate = thisDate
            #print(r)
            #print('here\'s the greatest increase in profit!\r')
        if thisProfit < greatestDecrease:
            greatestDecrease = thisProfit
            greatestDecreaseDate = thisDate
            #print(r)
            #print('here\'s the greatest decrease in profit!\r')
    averageProfitChange = totalProfitChange / totalMonths
    averageProfitChange = int(100 * averageProfitChange) / 100
    profitInfo = f'The total profit over all {totalMonths} months was {totalProfit}'
    increaseInfo = f'The largest increase occurred on {greatestIncreaseDate} and was ${greatestIncrease}'
    decreaseInfo = f'The largest decrease occurred on {greatestDecreaseDate} and was ${greatestDecrease}'
    profitChangeInfo = f'The total change in profit was {totalProfitChange} and the average change was {averageProfitChange}'

    analysisInfo = (profitInfo + '\n'
        + increaseInfo + '\n'
        + decreaseInfo + '\n'
        + profitChangeInfo)

    print(analysisInfo)
    file_object.write(analysisInfo)
    file_object.close()
