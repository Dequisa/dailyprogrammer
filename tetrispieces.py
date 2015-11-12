import random

tetris_pieces = ['O','I','S','Z','L','J','T']
final_list = [random.choice(tetris_pieces)]

def makebag():
    return sorted(tetris_pieces, key=lambda k: random.random())

def check_input(str_to_check):
    checklist = list(str_to_check)
    for x in range(0,6):
        for y in range(1,6):
            if checklist[7*x]==checklist[7*x+y]:
                print (x,y)
                return False
    return True

for x in range(0, 7):
    final_list =  makebag() + final_list


print ''.join(final_list)
print check_input(final_list)
