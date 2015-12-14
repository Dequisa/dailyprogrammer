primes = [2, 3, 5, 7, 11, 13]
num_to_check = 14

while len(primes) < 10001:
    isPrime = True
    for prime in primes:
        if num_to_check%prime == 0:
            isPrime = False
    if isPrime:
        primes.append(num_to_check)
        print num_to_check
    num_to_check += 1
    

print primes[10000]
