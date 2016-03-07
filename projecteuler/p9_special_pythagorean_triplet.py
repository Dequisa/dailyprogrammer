#encoding=utf-8
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#Runs in 0.484921 seconds
import time
import numpy

startTime = time.clock()
solution = (0,0)

def check(a,b):
    if (a**2 + b**2 == (1000-a-b)**2):
        return (a,b)
    else:
        return None

for x in range(1, 1000):
    for y in range(1, 1000):
        if check(x,y) != None:
            solution = (check(x,y))

c = 1000 - (sum(solution))

print solution[0] * solution[1] * c, time.clock() - startTime
