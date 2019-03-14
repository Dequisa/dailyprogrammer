#encoding=utf-8
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
#Runs in 12.438802 seconds

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
for prime in primesInRange(1000000):
    primeList.append(prime)

def distinctPrimeFactors(n):
    primeFactors = set()
    while n > 1:
        for prime in primeList:
            if n%prime == 0:
                primeFactors.add(prime)
                n = n/prime
                break
    return len(primeFactors)

isSolved = False
for x in xrange(0,1000000):
    for y in xrange(0,4):
        if distinctPrimeFactors(x+y)!=4:
            break
        if y == 3:
            isSolved = True

    if isSolved == True:
        print x, time.clock() - startTime
        break


