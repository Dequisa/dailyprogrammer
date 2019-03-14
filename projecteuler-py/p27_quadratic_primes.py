#encoding=utf-8
"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
#runtime = 0.40889 seconds
import numpy
import time
#Return a prime generator using the seive of eratosthenes.  Adapted from below
#http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primesInRange(limit):
    potentialPrimesList = [True] * limit
    potentialPrimesList[0] = potentialPrimesList[1] = False
    for index, isPrime in enumerate(potentialPrimesList):
        if isPrime is True:
            yield index
            for x in xrange(index*2, limit, index):
                potentialPrimesList[x] = False
startTime = time.clock()
primes  = set()
aValues = set()
bValues = []
maxConsequative = (0,0,0)

#b has to be prime.  If n =0, n^2 + an + b = b.  Primes are only positive
for prime in primesInRange(100000):
    primes.add(prime)
    if prime < 1000:
        bValues.append(prime)

#a's set can be reduced by half.  If n is 1, a + 1 + b is prime.  Also, a must be odd.
for prime in bValues:
    for a in range(-999,1000):
            if abs(a) < 1000 and a + prime + 1 in primes and a not in aValues and a%2 == 1:
                aValues.add(a)

def genericQuad(a,b,n):
    return n**2 + a*n + b

def countFuncConsequativePrimes(a,b):
    count = 0
    for n in xrange(0,100000):
        if genericQuad(a,b,n) in primes:
            count += 1
        else:
            return count

for a in aValues:
    for b in bValues:
        currentCount = countFuncConsequativePrimes(a,b)
        if currentCount > maxConsequative[0]:
            maxConsequative = (currentCount, a, b)

print maxConsequative[1] * maxConsequative[2], time.clock() - startTime


