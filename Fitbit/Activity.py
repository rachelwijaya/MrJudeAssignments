#Activity.csv exercise
import csv
import matplotlib.pyplot as plt
import datetime as dt
#import numpy as np
import statistics as st
import pandas as pd

path = "activity.csv"


dict, dictInterval, dictIntervalWeekDays, dictIntervalWeekEnds = {},{},{},{}
with open(path) as f:
    reader = csv.reader(f, delimiter = ",")
    header = next(reader)
    for row in reader:
        steps = row[0]
        if (steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
        
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))
                
            if (date2 % 7 == 0):
                dictIntervalWeekEnds.setdefault(interval, [])
                dictIntervalWeekEnds[interval].append(int(steps))
            else:
                dictIntervalWeekDays.setdefault(interval, [])
                dictIntervalWeekDays[interval].append(int(steps))

listDate, listTotal, listAve, listInterval,listIntervalMean = [],[],[],[],[]

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
    
plt.hist(listTotal, bins = 20)
plt.title("Total steps daily")
plt.xlabel("Number of steps")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))
plt.show()
  
print("The mean number of steps: ", st.mean(listTotal))
print("The median number of steps: ", st.median(sorted(listTotal)))

    
#PART B
for i in dictInterval.keys():
    listInterval.append(i)
for i in dictInterval.values():  
    listIntervalMean.append(st.mean(i))
        
plt.plot(listInterval,listIntervalMean)
plt.title("Average number of steps taken in an interval")
plt.xlabel("Interval")
plt.ylabel("Average no. of steps")
plt.show()
    
dictMaxInterval = {}
for i in listInterval:
    for j in listIntervalMean:
        dictMaxInterval[str(i)] = float(j)
    
    maxStepsInterval = max(listIntervalMean)
    print("Maximum steps in an interval: ", maxStepsInterval)

#PART C
df = pd.read_csv(path, NAValues = ["NA"], nonMissingValues = False)
totalNA = pd.isnull().sum().pd.notnull()
print(totalNA)
    
df.fillna(0)
plt.hist(listTotal, bins = 20)
plt.title("Total steps daily")
plt.xlabel("Number of steps")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))
plt.show()

#PART D
listKeysWeekdays, listValuesWeekdays, listKeysWeekends, listValuesWeekends = [],[],[],[]
for i in dictIntervalWeekDays.keys():
    listKeysWeekdays.append(i)
for i in dictIntervalWeekDays.values():
    listValuesWeekdays.append(i)
for i in dictIntervalWeekEnds.keys():
    listKeysWeekends.append(i)
for i in dictIntervalWeekEnds.values():
    listValuesWeekends.append(i)

plt.plot(listKeysWeekdays, listValuesWeekdays, listKeysWeekends, listValuesWeekends)
plt.title("Ave. no. of steps taken in weekdays in 5 minute intervals")
plt.xlabel("5 MINUTE INTERVAL")
plt.ylabel("Ave. no. of steps")
plt.show()

    

#%% 
