# Team duckingAwesome -- Yaru Luo & Emory Walsh
# SoftDev1 pd1
# K06 -- StI/O: Divine your Destiny!
# 2019-09-17


import csv, random

rows = []
with open('occupations.csv', 'r') as csvFile:
    csvreader = csv.reader(csvFile)
    for row in csvreader:
        rows.append(row)

dictionary = {}
for item in rows[1: len( rows) - 1]:
    key = item[0]
    value = float( item[1])
    dictionary[ key] = value



#returns a randomly selected occupation where the results
#are weighted by the percentage given
def randomOccupation():
    currentNo = 0
    currentOcc = ""
    randomNo = random.randint( 0, 998) #total % is 99.8
    for item in dictionary:
        currentOcc = item
        #parse through the dictionary until you reach
        #the random number, then return the occ
        currentNo += dictionary.get( item) * 10
        if currentNo >= randomNo:
            return currentOcc
    #return currentOcc

print( randomOccupation())
