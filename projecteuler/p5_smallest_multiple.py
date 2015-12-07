#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


"""""
def superDiv(n):
    isDivis = True
    for x in range(11, 21):
        if n%x != 0:
            isDivis = False
    return isDivis
""""" 

from __future__ import division

def primes_up_to(n):
    return_primes = []
    for x in range(2, n):
        isPrime = True
        for y in range(2, x):
            if x%y == 0:
                isPrime = False
        if isPrime == True:
            return_primes.append(x)
    return return_primes

extra_primes = [2,2,2,3]
        
factor_list = primes_up_to(21) + extra_primes

product = reduce(lambda x, y: x*y, factor_list)

def div_check(n):
    for x in range(1,21):
        print ("%d mod %d is %d") %(n,x,n%x)

div_check(product)


"""

solution = False
current_num = 670442572700
while solution == False:
    if superDiv(current_num):
        solution = True
    else:
        print "%d" %(current_num)
        current_num += 1

print current_num





#def get_common_factors(n):
#    for x in range(1, n + 1):
        
"""
