#encoding=utf-8
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
#Runs in 0.033505 seconds
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
for prime in primesInRange(100000):
    primeList.append(prime)

def biggestPrimeFactor(n):
    biggestPrime = 0
    for prime in primeList:
        if n%prime == 0:
            n = n/prime
            if prime > biggestPrime:
                biggestPrime = prime
    return biggestPrime


print biggestPrimeFactor(600851475143), time.clock()-startTime



