#https://www.hackerrank.com/challenges/simple-array-sum
"""
You are given an array of integers of size NN. Can you find the sum of the elements in the array?
"""
numberOfElements = int(raw_input().strip())

array = map(int, raw_input().split(' '))

print sum(array)
