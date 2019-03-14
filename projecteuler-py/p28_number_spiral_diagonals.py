#encoding=utf-8
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time
import numpy

"""
Recursive solution.  We know that f(n) = f(n-2) + the four new numbers (only odd numbers can make spirals).
To find the first new number of each larger spiral, I wrote out the first four and saw the pattern:
x|y
---
3|3
5|13
7|31
9|57

The parabola  f(x) = (n * (n-2)) - (n-3) = n^2 -3n + 3 explains this relation.
To find the sum of all 4 new numbers, I added (n-1) to the first term 1,2 or 3 times (from looking at the relationship from one corner to the next).
This yielded the recurrent relation below
"""
#runtime = 0.000405 seconds

def getSpiralDiags(n):
    if n == 1:
        return 1
    return getSpiralDiags(n-2) + 4*n**2 - (6*n) + 6

startTime = time.clock()
print getSpiralDiags(1001), time.clock()-startTime
