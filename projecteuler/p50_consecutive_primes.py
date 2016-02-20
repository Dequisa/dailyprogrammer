#encoding=utf-8
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
#Runtime = 0.885911 seconds

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

primeSet = set(primeList)
maxPrime = (0,0)

for startingIndex in xrange(0,len(primeList)):
    runningTotal = 0
    count = 0
    for primeIndex in xrange(startingIndex, len(primeList) - startingIndex):
        runningTotal += primeList[primeIndex]
        count += 1
        if runningTotal in primeSet and count > maxPrime[1]:
            maxPrime = (runningTotal, count)
        if runningTotal > 1000000:
            break

print maxPrime, time.clock()-startTime
