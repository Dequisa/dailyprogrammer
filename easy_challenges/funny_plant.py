def rec(n):
    if n < 3:
        return 1
    if n == 3:
        return 3
    else:
        return 3*rec(n-1) - rec(n-2)

people = input("How many people do you want to feed?: ")
start_num = input("How many plants do you start with?: ")

fruit = 0
week = 0

while people >= fruit:
    week += 1
    fruit = start_num * rec(week)

print week
