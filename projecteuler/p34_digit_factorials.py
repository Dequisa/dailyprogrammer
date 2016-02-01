#encoding=utf-8
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
factorialDict = {}

def factorial(n):
    if n == 0:
        return 1
    if n in factorialDict:
        return factorialDict[n]
    else:
        nFactorial = n * factorial(n-1)
        factorialDict[n] = nFactorial
        return nFactorial

def isCurious(n):
    factorialDigitSum = 0
    for number in list(str(n)):
        factorialDigitSum += factorial(int(number))
    return factorialDigitSum==n

for n in xrange(2,100000):
    if isCurious(n):
        print n

