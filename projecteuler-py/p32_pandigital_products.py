#encoding=utf-8
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from itertools import permutations
import time

startTime = time.clock()
productList = set()
oneThroughNine = [1,2,3,4,5,6,7,8,9]

def pandigitalCheck(tuple):
    tupleList = list(tuple)
    for x in xrange(0, len(tupleList)):
        tupleList[x] = str(tupleList[x])
    for multIndex in xrange(1,7):
        equalsIndex = multIndex + 1
        while equalsIndex < 8:
            if int(''.join(tupleList[:multIndex])) * int(''.join(tupleList[multIndex:equalsIndex])) == int(''.join(tupleList[equalsIndex:])):
                productList.add(int(''.join(tupleList[equalsIndex:])))
            equalsIndex += 1

for tuple in permutations(oneThroughNine,9):
    pandigitalCheck(tuple)

print sum(productList), time.clock()-startTime





















