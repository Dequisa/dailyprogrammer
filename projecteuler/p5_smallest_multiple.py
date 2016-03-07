#encoding=utf-8
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#Runs in 0.000129 seconds
import time

startTime = time.clock()
primes = [2,3,5,7,11,13,17,19]
primeFactorsOfProduct = {}
finalProduct = 1

def primeFactors(n):
    factors = {}
    for prime in primes:
        while n%prime==0:
            n = n/prime
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1
    return factors

for x in xrange(2,21):
    for key in primeFactors(x):
        if key not in primeFactorsOfProduct:
            primeFactorsOfProduct[key] = primeFactors(x)[key]
        elif primeFactorsOfProduct[key] < primeFactors(x)[key]:
            primeFactorsOfProduct[key] = primeFactors(x)[key]

for key in primeFactorsOfProduct:
    for x in xrange(0,primeFactorsOfProduct[key]):
        finalProduct = finalProduct * key

print finalProduct, time.clock()-startTime
