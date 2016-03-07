#encoding=utf-8
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# x | f(x)
# --------
# 1 | 1**2 - 1**2 = 0
# 2 | (1+2)**2 - (1**2+2**2) = 3**2 - (1+4) = 9 - 5 = 4
# 3 | (1+2+3)**2 - (5 + 3**2) = 6**2 - (5+6)= 36-11 = 25
# n | n**2 * n-1 + f(x-1)

#Runs in 0.000107 seconds

import numpy
import time

startTime = time.clock()

def getDifference(n):
    if n == 1:
        return 0
    if n == 2:
        return 4
    else:
        return ((n**2)*(n-1) + getDifference(n-1))

print getDifference(100), time.clock() - startTime
