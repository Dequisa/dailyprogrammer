#encoding=utf-8
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
#Runs in 0.706214 seconds
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
for prime in primesInRange(2000000):
    primeList.append(prime)

print sum(primeList), time.clock()-startTime
