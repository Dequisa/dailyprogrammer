#encoding=utf-8
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
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

#primeList = [1487]

isSolution = False
for prime in primeList:
    print prime
    for incrementValue in xrange(1,3500):
        if prime + incrementValue in primeList and set(str((prime + incrementValue))) == set(str(prime)):
            for multiplier in xrange(1,4):
                if (prime + (multiplier * incrementValue) not in primeList) or set(str((prime + multiplier * incrementValue))) != set(str(prime)):
                    break
                if multiplier == 3:
                    print prime, incrementValue

    if isSolution:
        break
