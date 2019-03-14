#encoding=utf-8
"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
#Made a binary converter for fun.  bin() would work much faster.
#Runs in 2.469011 seconds
import numpy
import time
startTime = time.clock()
binaryList = []
palindromeList = []

for x in xrange(22):
    binaryList.append(2**x)

def isPalindrome(numberList):
    original = []
    for number in numberList:
        original.append(number)
    numberList.reverse()
    return original == numberList

def truncate(binaryNum):
    for index, digit in enumerate(binaryNum):
        if digit == 1:
            binaryNum = binaryNum[index:]
            break
    return binaryNum

def decToBinary(decimalNumber):
    binaryNum = [0] * 40
    while decimalNumber != 0:
        for index, powerOfTwo in enumerate(binaryList):
            if powerOfTwo > decimalNumber:
                binaryNum[index-1] = 1
                decimalNumber = decimalNumber - binaryList[index-1]
                break
    binaryNum.reverse()
    return truncate(binaryNum)

for x in xrange(1000000):
    if isPalindrome(list(str(x))) and isPalindrome(decToBinary(x)):
        palindromeList.append(x)

print sum(palindromeList), time.clock()-startTime
