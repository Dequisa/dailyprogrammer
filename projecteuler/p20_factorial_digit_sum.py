# coding=utf-8
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

def factorial(int):
    if int == 1:
        return int
    else:
        return int * factorial(int-1)

sum = 0

#for number in list(str(factorial(1000))):
#    sum += int(number)

#print sum

def func(n):
    print n
    return func(n +1)

func(0)
