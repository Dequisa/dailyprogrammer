#encoding=utf-8
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
#Runs in 0.104016 seconds
import numpy
import time

startTime = time.clock()
cheweyConstant = ''
n = 1

while len(cheweyConstant) < 1000002:
    cheweyConstant = cheweyConstant + (str(n))
    n += 1

bigProduct = 1

for x in xrange(0,7):
    bigProduct = bigProduct * int(cheweyConstant[(10**x)-1])

print bigProduct, time.clock()-startTime
