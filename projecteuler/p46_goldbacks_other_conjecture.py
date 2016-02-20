#encoding=utf-8
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
#Runs in 14.56638 seconds
import numpy
import time

startTime = time.clock()

def primesInRange(limit):
    potentialPrimesList = [True] * limit
    potentialPrimesList[0] = potentialPrimesList[1] = False
    for index, isPrime in enumerate(potentialPrimesList):
        if isPrime is True:
            yield index
            for x in xrange(index*2, limit, index):
                potentialPrimesList[x] = False
primeList = []
for prime in primesInRange(10000):
    primeList.append(prime)

twiceSquareList = []
for a in xrange(1,10000):
    twiceSquareList.append(2 * a**2)

for x in xrange(9,10000,2):
    primeIndex = 0
    hasSolution = False
    while x > primeList[primeIndex]:
        squareIndex = 0
        while twiceSquareList[squareIndex] < x:
            if x == primeList[primeIndex] + twiceSquareList[squareIndex]:
                hasSolution = True
                break
            squareIndex += 1
        primeIndex += 1
    if hasSolution == False and x not in primeList:
        print x, time.clock() - startTime
        break
