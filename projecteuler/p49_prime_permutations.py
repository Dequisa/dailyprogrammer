#encoding=utf-8
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
#Runs in 1.647033 seconds
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
    if prime > 999:
        primeList.append(prime)

isSolution = False
for prime in primeList:
    for incrementValue in xrange(10,3500,10):  #We step by 10, because adding any other number would change the digits.
        if (prime + incrementValue) in primeList and set(str((prime + incrementValue))) == set(str(prime)):
            for multiplier in xrange(0,3):
                if (prime + (multiplier * incrementValue) not in primeList) or set(str((prime + multiplier * incrementValue))) != set(str(prime)):
                    break
                if multiplier == 2 and prime!=1487:
                    print str(prime) + str(prime + incrementValue) + str(prime + 2 * incrementValue), time.clock()-startTime
                    isSolution = True

    if isSolution:
        break
