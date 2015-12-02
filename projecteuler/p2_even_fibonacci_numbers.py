total = 0
n = 1
x = 1

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def evenfib(n):
    if fib(n)%2 == 0:
        return fib(n)
    else:
        return 0

while x < 4000000:
    total += evenfib(n)
    x = fib(n)
    n += 1

print total
