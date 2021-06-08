import csv
import math

#Opening the file
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data.pop(0)

#Finding the mean
def findMean(data):
    length = len(data)
    sum = 0 

    for i in data:
        sum = sum + int(i)
    
    mean = sum/length
    return mean

mean = findMean(data)

#Squaring the list
squaredList = []
for i in data:
    squaredNo = (int(i) - mean)**2
    squaredList.append(squaredNo)

#Adding all the numbers
sum = 0
for i in squaredList:
    sum = sum + i

#Finding the square root
squareRoot = sum/(len(data)-1)

#Finding the standard deviation
standardDeviation = math.sqrt(squareRoot)
print(standardDeviation)