solution = False
primes = []

#Creates a list of tuples up to a number.  (number, isPrime)
def primes_in_range(limit):
    numbers_in_range = []
    for x in range(2, limit + 1):
        numbers_in_range.append((x, True))

    prime_num = 2
    index = 0

    while prime_num * prime_num < limit:

        n = 1

        while n * prime_num <= limit:

            if numbers_in_range[prime_num * n - 2][0] != prime_num:
                numbers_in_range[prime_num * n - 2] = (n*prime_num, False)
            n += 1

        for m in range(index + 1, len(numbers_in_range)):
            if numbers_in_range[m][1] is True:
                prime_num = numbers_in_range[m][0]
                index = m
                break

    return numbers_in_range

for tuple in primes_in_range(100000):
    if tuple[1] == True:
        primes.append(tuple[0])

def getExponent(n, prime_factors):
    exponent = 0
    for prime in prime_factors:
        if prime == n:
            exponent += 1
    return exponent

def getdivisornum(n):
    prime_factors = []
    considered_primes = []
    prime_exponents = []
    final_list = []


    for prime in primes:
        while n%prime == 0:
            prime_factors.append(prime)
            n = n/prime
        if n ==1:
            break

 Creates a list of exponents of primes in prime_factors
    for prime in prime_factors:
        if prime not in considered_primes:
            considered_primes.append(prime)
            prime_exponents.append(getExponent(prime, prime_factors))
    for prime in prime_exponents:
        final_list.append(prime + 1)

    return reduce(lambda x,y: (x*y), final_list)

n = 2        
while solution ==False:
    current_number = (n * (n + 1))/2
    current_divisors = getdivisornum(current_number)

    print (current_number, current_divisors)

    if current_divisors > 500:
        solution = True
        print current_number
    n += 1
