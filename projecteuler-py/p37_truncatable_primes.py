#encoding=utf-8
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
def rightTruncatePrime(prime):
    if prime not in primeSet:
        return False
    if prime < 10:
        return prime in primeSet
    return rightTruncatePrime(int(''.join(list(str(prime)))[:-1]))

def leftTruncatePrime(prime):
    if prime not in primeSet:
        return False
    if prime < 10:
        return prime in primeSet
    return leftTruncatePrime(int(''.join(list(str(prime)))[1:]))

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

truncatablePrimes = []

for prime in primeList:
    if prime > 9 and rightTruncatePrime(prime) and leftTruncatePrime(prime):
        truncatablePrimes.append(prime)
        print truncatablePrimes
    if len(truncatablePrimes)==11:
        break

print truncatablePrimes
print sum(truncatablePrimes)
