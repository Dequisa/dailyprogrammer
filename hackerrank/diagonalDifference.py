#https://www.hackerrank.com/challenges/diagonal-difference
#encoding=utf-8
"""
Given a square matrix of size N×N, calculate the absolute difference between the sums of its diagonals.
"""

numberOfRows = int(raw_input().strip())

matrix = []
for row in xrange(0,numberOfRows):
    row = map(int,raw_input().strip().split(' '))
    matrix.append(row)

diagOneSum = 0
diagTwoSum = 0

for count,x in enumerate(xrange(0, numberOfRows)):
    diagOneSum += matrix[x][count]
    diagTwoSum += matrix[x][numberOfRows-1-count]
    count += 1

print abs(diagOneSum - diagTwoSum)
