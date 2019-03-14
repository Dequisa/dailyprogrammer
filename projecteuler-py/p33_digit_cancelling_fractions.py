#encoding=utf-8
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from __future__ import division

numeratorProduct = 1
denominatorProduct = 1

def isCurious(numerator,denominator):
    numerList = list(str(numerator))
    denomList = list(str(denominator))
    if len(set(numerList) | set(denomList)) == 3:
        commonNumberList = list((set(numerList) & set(denomList)))
        if len(commonNumberList) != 0:
            commonNumber = commonNumberList[0]
            numerList.remove(str(commonNumber))
            denomList.remove(str(commonNumber))
            if int(commonNumber) != 0 and int(denomList[0]) != 0 and int(numerList[0])/int(denomList[0]) == numerator/denominator:
                return True
    return False

for numerator in xrange(10,100):
    for denominator in xrange(numerator+1,100):
        if isCurious(numerator,denominator):
            numeratorProduct = numeratorProduct * numerator
            denominatorProduct = denominatorProduct * denominator 

print numeratorProduct/denominatorProduct
