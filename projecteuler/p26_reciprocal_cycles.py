#encoding=utf-8
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import operator
import time
startTime = time.clock()

denomToRepeatSizeDict = {}

def repeatCheck(denom,quotient):
    for x in range(6,int(len(quotient)/2) +1):
        if quotient[-x:] == quotient[len(quotient)-(2*x):len(quotient)-x]:
            denomToRepeatSizeDict[denom] = x
            return True
    return False

def properDivide(num, denom):
    quotient = []
    updatingNum = num
    while updatingNum != 0:
        quotient.append(divmod(updatingNum*10,denom)[0])
        updatingNum = (divmod(updatingNum*10,denom)[1]) 
        if len(quotient) >= 30:
            if repeatCheck(denom, quotient):
                break
    return quotient

for x in range(1,1000):
    properDivide(1,x)

print max(denomToRepeatSizeDict.iteritems(), key = operator.itemgetter(1))[0], time.clock() - startTime
