primes = []

#for x in range(2,600851475143):
for x in range(2, 100000):
    isPrime = True
    for y in range(2, x):
        if x%y == 0:
            isPrime = False
    if isPrime:
        primes.append(x)

#def largest_prime(n):
#    for x in primes:
#        if n%x == 0 and n=x

print primes

#600851475143
