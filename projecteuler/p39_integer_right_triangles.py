#encoding=utf-8
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
#Runtime 46.272908 seconds.  Not good.  Will try to come back and optimize later.
import numpy
import time

startTime = time.clock()
maxP = (3,120)

def solutionsByPerimeter(p):
    solutionSet = [set()]
    numberOfSolutions = 0
    for a in xrange(1,p/2):
        for b in xrange(1,p-1):
            if a + b > p:
                break
            if p == a + b + ((a**2+b**2))**.5 and set([a,b]) not in solutionSet:
                solutionSet.append(set([a,b]))
                numberOfSolutions += 1
    return numberOfSolutions

for p in xrange(1,1001):
    pSolutions = solutionsByPerimeter(p)
    if pSolutions > maxP[0]:
        maxP = (pSolutions, p)

print maxP, time.clock()-startTime
