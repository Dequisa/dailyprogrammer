#digits = input("How many digits would you like in the number?: ")
#fangs_num = input("How many fangs would you like to have?: ")

def twodigitfactors(num):
    factors_list = []
    for x in range(1,num+1):
        if num%x == 0 and len(str(x)) == 2:
            factors_list.append(x)        
    return factors_list


print twodigitfactors(5343)
