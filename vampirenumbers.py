digits = input("How many digits would you like in the number?: ")
fangs_num = input("How many fangs would you like to have?: ")
vampire_list = []

def twodigitfactors(num):
    factors_list = []
    for x in range(1,num+1):
        if num%x == 0 and len(str(x)) == 2:
            factors_list.append(x)        
    return factors_list


for x in range (10**(digits-1), 10**digits):
    okfactors = []
    is_duplicate = False
    for factor in twodigitfactors(x):
        if set(str(factor)).issubset(set(str(x))):
            okfactors.append(factor)
    if fangs_num == 2:
        for number in range(0,len(okfactors)):
            for number2 in range(0, len(okfactors)):
                if okfactors[number] * okfactors[number2] == x and sorted(str(okfactors[number]) + str(okfactors[number2])) == sorted(str(x)) and is_duplicate == False:
                    vampire_list.append([x, okfactors[number], okfactors[number2]])
                    is_duplicate = True

    if fangs_num == 3:
        for a in range(0, len(okfactors)):
            for b in range(0, len(okfactors)):
                for c in range(0, len(okfactors)):
                    if okfactors[a] * okfactors[b] * okfactors[c]  == x and sorted(str(okfactors[a]) + str(okfactors[b]) + str(okfactors[c])) == sorted(str(x)) and is_duplicate == False:
                        vampire_list.append([x, okfactors[a], okfactors[b], okfactors[c]])
                        is_duplicate = True

print(vampire_list)
                
