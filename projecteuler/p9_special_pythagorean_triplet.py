import numpy

solution = (0,0)

def check(a,b):
    if (a**2 + b**2 == (1000-a-b)**2):
        return (a,b)
    else:
        return None

for x in range(1, 1000):
    for y in range(1, 1000):
        if check(x,y) != None:
            solution = (check(x,y))

c = 1000 - (sum(solution))

print solution[0] * solution[1] * c
