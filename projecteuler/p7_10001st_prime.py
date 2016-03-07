"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
#Runs in 0.296031 seconds
import time
import numpy

startTime = time.clock()

def primesInRange(limit):
    potentialPrimes = limit * [True]
    for index in xrange(2, limit):
        if potentialPrimes[index]:
            yield index
            for y in xrange(2 * index, limit, index):
                potentialPrimes[y] = False

primeList = []
for element in primesInRange(1000000):
    primeList.append(element)

print primeList[10000], time.clock()-startTime

