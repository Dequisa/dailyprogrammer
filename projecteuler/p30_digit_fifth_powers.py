#encoding=utf-8
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import time
import numpy

startTime = time.clock()
powerNumbers = []

#Capped at 6 digit numbers.  The biggest possible sum of 5th powers of a 7 digit number is 413343 (a 6-digit number)
for n in xrange(10,1000000):
    numberList = list(str(n))
    total = 0
    for number in numberList:
        total += int(number)**5
    if total == n:
        powerNumbers.append(total)

print sum(powerNumbers), time.clock()-startTime
