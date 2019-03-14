import numpy

twoThousandthed = 2**1000

total = 0

for x in range(0,400):
    digit = (twoThousandthed%10**(x+1))/(10**x)
    total += digit
    print digit
    print total

print total
