#encoding=utf-8
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
#runtime = 0.096113 seconds
import time
startTime = time.clock()
currentMax = 0

def pandigitalCheck(number):
    if len(list(str(number))) != 9 or set(list(str(number))) != set(list(str(123456789))):
        return False
    return True

for x in xrange(191,10000):
    pandigitalNumber = str(x)
    for y in xrange(2,5):
        if len(pandigitalNumber) > 9:
            break
        if pandigitalCheck(int(pandigitalNumber)) and int(pandigitalNumber) > currentMax:
            currentMax = int(pandigitalNumber)
            break
        pandigitalNumber = pandigitalNumber + str(x * y)
            
print currentMax, time.clock()
