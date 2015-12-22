primes = []

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

for tuple in primes_in_range(2000000):
    if tuple[1] == True:
        primes.append(tuple[0])


print sum(primes)

