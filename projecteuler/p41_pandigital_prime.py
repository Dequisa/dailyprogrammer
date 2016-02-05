#encoding=utf-8
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
#runtime: 1345.62276 seconds.  Need to revisit
import time

startTime = time.clock()

def isPandigital(n):
    return  set(range(1,len(list(str(n)))+1)) == set(list(int(char) for char in list(str(n))))

def pandigitalPrimesInRange(limit):
    potentialPrimes = [True] * limit
    potentialPrimes[0] = potentialPrimes[1] = False
    for index, primeCandidate in enumerate(potentialPrimes):
        if primeCandidate:
            if isPandigital(index):
                yield index
            for multipleOfPrime in xrange(index *2, limit, index):
                potentialPrimes[multipleOfPrime] = False

primeList = []
for prime in pandigitalPrimesInRange(1000000000):
    primeList.append(prime)
    print prime

max = 0

for prime in primeList:
    if prime > max:
        max = prime

print max, time.clock()-startTime
