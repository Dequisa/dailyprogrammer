input_text = open("/Users/benstone/Desktop/dailyprogrammer/ruthaaroninput.txt")
primes_file = open("/Users/benstone/Desktop/dailyprogrammer/primes_list.txt")
primes = map(int, primes_file.read().split(", "))
pair_number = int(input_text.readline())

def primefactors(list):
    uniqueprimefactors = []
    list_as_int = 0
    list_as_int = int(''.join(list))
    for checkprime in primes:
        if list_as_int%checkprime == 0:
            uniqueprimefactors.append(checkprime)
    return uniqueprimefactors

def ruthaaroncheck(list_one, list_two):
    total1 = 0
    total2 = 0
    for digit1 in list_one:
        total1 = total1 + int(digit1)
    for digit2 in list_two:
        total2 = total2 + int(digit2)
    if total1 == total2:
        return True
    else:
        return False

for x in range(0, pair_number):
    first_number = []
    second_number = []
    isfirstnum = True
    for char in input_text.readline():
        if char.isdigit() and isfirstnum:
            first_number.append(char)
        elif char == ',':
            isfirstnum = False
        if char.isdigit() and not isfirstnum:
            second_number.append(char)
    if ruthaaroncheck(primefactors(first_number), primefactors(second_number)):
        print "(%s,%s) is valid!" % (''.join(first_number), ''.join(second_number))
    else:
        print "(%s,%s) is not valid :(" % (''.join(first_number), ''.join(second_number))
