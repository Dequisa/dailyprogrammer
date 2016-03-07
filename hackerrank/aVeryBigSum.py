#https://www.hackerrank.com/challenges/a-very-big-sum
"""
You are given an array of integers of size N. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.
"""

numberOfLines = int(raw_input().strip())
array = map(int, raw_input().strip().split(' '))
print sum(array)
