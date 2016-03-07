#encoding=utf-8
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
#Runtime = 0.000126 seconds
import time

startTime = time.clock()

def sum_mults(n):
    x = 1
    total = 0
    while x*n < 1000:
        total += (x * n)
        x += 1    
    return total

print sum_mults(3) + sum_mults(5) - sum_mults(15), time.clock()-startTime
