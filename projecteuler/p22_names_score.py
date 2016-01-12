#coding=UTF-8
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
namesList = []
letterValueDict = {}
finalTotal = 0

for x in range(0,26):
    letterValueDict[alphabet[x]] = x + 1

with open("p022_names.txt") as csvfile:
    reader = csv.reader(csvfile)
    for name in reader:
        namesList = name
        
sortedNames = sorted(namesList)

def valueOf(name, position):
    total = 0
    for letter in list(name):
        total += letterValueDict[letter]
    return total * position

for idx, name in enumerate(sortedNames):
    finalTotal += valueOf(name, idx + 1)

print finalTotal


"""names = bigString.split(',')

for name in names:
    name = name[2:-1]

print names
"""
