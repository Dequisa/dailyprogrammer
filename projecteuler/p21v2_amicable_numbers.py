#coding=utf-8                                                                                                                                                                        
"""                                                                                                                                                                                 Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).                                                                             
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.                                                            
                                                                                                                                                                                    
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
                                                                                                                                                                                     
Evaluate the sum of all the amicable numbers under 10000.                                                                                                                            
"""

import numpy

amicableList = []
divisorSumDict = {}

def isAmicable(a,b):
    return divisorSumDict[a] == b and divisorSumDict[b] == a and a != b

def sumAllDivisors(n):
    list = []
    for possibleDivisor in range(1, int(n**.5) + 1):
        if n%possibleDivisor == 0:
            list.append(possibleDivisor)
            if possibleDivisor != n/possibleDivisor and n/possibleDivisor != n:
                list.append(n/possibleDivisor)
    return sum(list)

for x in range(0,10000):
    divisorSumDict[x] = sumAllDivisors(x)

for x in range(0,10000):
    for y in range(0,10000):
        print x,y
        if isAmicable(x,y):
            amicableList.append(y)


print amicableList
print sum(amicableList)


