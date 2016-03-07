#https://www.hackerrank.com/challenges/plus-minus
"""
Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. Print the decimal value of each fraction.
"""


numberOfElements = float(raw_input().strip())
array = map(int, raw_input().strip().split(' '))

positiveCount = 0
negativeCount = 0
zeroCount = 0

for element in array:
    if element > 0:
        positiveCount += 1
    elif element < 0:
        negativeCount += 1
    elif element == 0:
        zeroCount += 1

print positiveCount/numberOfElements,'\n', negativeCount/numberOfElements,'\n', zeroCount/numberOfElements, '\n'
