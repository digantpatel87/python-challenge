import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')
txtfilepath = os.path.join('analysis','finalresult.txt')

#set the counters and default values
Monthcounter = 0
Total = 0
RunningValue = 0
firstrun = 0
RunningChange = 0
TotalChange = 0
NumberOfChange = 0
AverageChange = 0.00
GreatestIncrease = 0
GreatestDecrease = 0
GreatestMonthIncrease = ""
GreatestMonthDecrease = ""

with open(csvpath) as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=',')

    #remove header
    header = next(csvreader)

    #loop for each row to count number of months
    for row in csvreader:
        #Number of records counter
        Monthcounter = Monthcounter + 1
        #add running profit/loss to total
        Total = Total + int(row[1])
       
        #check if the runningvalue is not 0 
        if RunningValue != 0:
            #get the difference between current and last value
            RunningChange =  int(row[1]) - RunningValue  
            #add the changes between previous and current on every loop
            TotalChange = TotalChange + RunningChange
            #add number of changes happen
            NumberOfChange = NumberOfChange + 1

            #check if the change is greater then previous change
            if (RunningChange > GreatestIncrease):
                GreatestIncrease = RunningChange
                GreatestMonthIncrease = row[0]

            #check if the change is less then previous change
            if (RunningChange < GreatestDecrease):
                GreatestDecrease = RunningChange
                GreatestMonthDecrease = row[0]

        #set the running number
        RunningValue = int(row[1])
    
#Set the average
AverageChange = round(TotalChange/NumberOfChange,2)
    
print(f"Financial Analysis")
print(f"----------------------")
print(f"Total Months: {Monthcounter}")
print(f"Total: {Total}")
print(f"Average  Change: {AverageChange}")
print(f"Greatest Increase in Profits: {GreatestMonthIncrease} ({GreatestIncrease})")
print(f"Greatest Decrease in Profits: {GreatestMonthDecrease} ({GreatestDecrease})")
print("```")

outputtxtfile = open(txtfilepath,'w+')
outputtxtfile.write(f"Financial Analysis \n")
outputtxtfile.write(f"----------------------\n")
outputtxtfile.write(f"Total Months: {Monthcounter}\n")
outputtxtfile.write(f"Total: {Total}\n")
outputtxtfile.write(f"Average  Change: {AverageChange}\n")
outputtxtfile.write(f"Greatest Increase in Profits: {GreatestMonthIncrease} ({GreatestIncrease})\n")
outputtxtfile.write(f"Greatest Decrease in Profits: {GreatestMonthDecrease} ({GreatestDecrease})\n")
outputtxtfile.write("```")
