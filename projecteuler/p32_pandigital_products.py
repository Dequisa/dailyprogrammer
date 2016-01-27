#encoding=utf-8
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
productList = set()

oneThroughNine = set([1,2,3,4,5,6,7,8,9])


for x in xrange(0,999999999):
    xSet = set([int(n) for n in str(x)])
    for y in xrange(0,999999999):
        ySet = set([int(n) for n in str(y)])
        productSet = set([int(n) for n in str(x*y)])
        allNumbers = xSet | ySet | productSet
        totalLength = len(xSet) + len(ySet) + len(productSet)
        if totalLength == 9 and oneThroughNine == allNumbers:
            productList.add(x*y)

print sum(productList)













