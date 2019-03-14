#encoding=utf-8
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
#Runs in 0.560243 seconds
import time

startTime = time.clock()

circularPrimes = []

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

primeSet = set(primeList)

def isCircular(prime):
    primeList = list(str(prime))
    for x in xrange(len(primeList)):
        primeList.insert(0,primeList[-1])
        del primeList[-1]
        if int(''.join(primeList)) not in primeSet:
            return False
    return True

for prime in primeList:
    if isCircular(prime):
        circularPrimes.append(prime)

print len(circularPrimes), time.clock()-startTime


