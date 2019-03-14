#coding=utf-8
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import numpy

amicableList = []

def sumAllDivisors(n):
    list = []
    for possibleDivisor in range(1, int(n**.5) + 1):
        if n%possibleDivisor == 0:
            list.append(possibleDivisor)
            if possibleDivisor != n/possibleDivisor and n/possibleDivisor != n:
                list.append(n/possibleDivisor)
    return sum(list)

for a in range(0,10000):
    b = sumAllDivisors(a)
    if sumAllDivisors(b) == a and a != b:
        amicableList.append(a)

print amicableList
print sum(amicableList)

                      

"""

def primeFactorization(n):
    array = [1]
    while n>1:
        for prime in primes:
            while n%prime == 0:
              array.append(prime)
              n = n/prime              
    return array
              
def getAllFactors(primesList):
    list = []
    for x in range(1,len(primesList)):
        for combination in itertools.combinations(primesList,x):
            if (reduce(lambda a,b:a*b, combination)) not in list:
                list.append(reduce(lambda a,b:a*b, combination))
    return list

def sumOfDivisors(n):
    #return sum([x for x in range(1,(n/2) + 1) if n%x==0])
    return sum(getAllFactors(primeFactorization(n)))


#print sum(amicableNumberTuple[0] for amicableNumberTuple in [(x,y) for x in range(1,10000) for y in range(1,10000) if isAmicable(x,y)]   )

amicableList = []

for x in range(0,1000):
    for y in range(0,1000):
        print x,y
        if isAmicable(x,y):
            amicableList.append(y)
            print amicableList

print amicableList

print sum(amicableList)

"""

