#encoding=utf-8
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
#Runtime = 
import time

startTime = time.clock()

fibDict = {}

def fib(n):
    if n == 0:
        return 1
    if n==1:
        return 2
    if n in fibDict:
        return fibDict[n]
    fibDict[n] = fib(n-1) + fib(n-2)
    return fibDict[n]

#fix this
while True:
 
    currentTerm = fib(n)
    n += 1

print total, time.clock()-startTime
