#encoding=utf-8
"""
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time

startTime = time.clock()
fibNumberDict = {1:1, 2:1, 3:2, 4:3, 5:5}

def getFibNumber(n):
    currentFib = fibNumberDict[n-1] + fibNumberDict[n-2]
    fibNumberDict[n] = currentFib
    return currentFib

for x in range(3,100000):
    getFibNumber(x)
    if len(str(fibNumberDict[x])) == 1000:
        print x, fibNumberDict[x], time.clock() - startTime
        break


