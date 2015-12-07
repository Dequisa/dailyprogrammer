#Recursive solution

import numpy

def get_difference(n):
    if n == 1:
        return 0
    if n == 2:
        return 4
    else:
        return ((n**2)*(n-1) + get_difference(n-1))

print get_difference(100)
