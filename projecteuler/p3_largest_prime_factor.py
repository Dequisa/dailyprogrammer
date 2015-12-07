primes = []
prime_factors = []

for x in range(2, 100000):
    isPrime = True
    for y in range(2, x):
        if x%y == 0:
            isPrime = False
    if isPrime:
        primes.append(x)

def primefactors(n):
    for prime in primes:
        print ("Looking at %d") %(prime)
        if n%prime == 0:
            prime_factors.append(prime)
            n = n/prime
    return prime_factors


print primefactors(600851475143)



