#coding=utf-8
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

primes = []

def sumOfDivisors(n):
    return sum([x for x in range(1,(n/2) + 1) if n%x==0])

def isAmicable(a,b):
    return sumOfDivisors(a) == b and sumOfDivisors(b) == a and a != b

def primeFactorization(n):
    array = []
    while n>1:
        for prime in primes:
            while n%prime:
              array.append(prime)
              

print sum(amicableNumberTuple[0] for amicableNumberTuple in [(x,y) for x in range(1,10000) for y in range(1,10000) if isAmicable(x,y)]   )

#amicableList = []

#for x in range(0,10000):
#    for y in range(0,10000):
#        print x,y
#        if isAmicable(x,y):
#            amicableList.append(y)
#            print amicableList

#print amicableList

#print sum(amicableList)


