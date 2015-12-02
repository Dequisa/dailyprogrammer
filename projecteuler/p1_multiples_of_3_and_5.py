def sum_mults(n):
    x = 1
    total = 0
    while x*n < 1000:
        total += (x * n)
        x += 1    
    return total

print sum_mults(3) + sum_mults(5) - sum_mults(15)
