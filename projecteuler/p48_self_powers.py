#encoding=utf-8
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
#Runs in 0.01103 seconds

import numpy
import time

startTime = time.clock()

enormousSum = 0
for x in xrange(1,1001):
    enormousSum += x**x

print str(enormousSum)[-10:], time.clock()-startTime

