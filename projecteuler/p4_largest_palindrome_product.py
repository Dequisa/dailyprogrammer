#encoding=utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#Runs in 2.914292 seconds

import time

startTime = time.clock()

def isPalindrome(n): 
    reg_n = list(str(n))
    rev_n = list(str(n))
    rev_n.reverse()
    return int(''.join(reg_n)) == int(''.join(rev_n))

biggest = 0

for x in range(100,999):
    for y in range(100,999):
        if isPalindrome(x*y) and x*y > biggest:
            biggest = x*y

print biggest, time.clock()-startTime




