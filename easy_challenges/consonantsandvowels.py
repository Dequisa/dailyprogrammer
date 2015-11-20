import random
final_word = ''
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
good_inputs = ['c','C','v','V']
input_ok = False

def getrandc():
    return random.choice(consonants)

def getrandv():
    return random.choice(vowels)

while input_ok is False:
    user_input = raw_input("Please enter a string of c's and v's: ")    
    if not set(user_input).issubset(set(good_inputs)):
        print("Only enter a string of c's and v's.  Uppercase is fine.")
    else:
        input_ok = True

for letter in user_input:
    if letter == 'c':
        final_word = final_word + getrandc()
    if letter == 'C':
        final_word = final_word + getrandc().upper()
    if letter == 'v':
        final_word = final_word + getrandv()
    if letter == 'V':
        final_word = final_word + getrandv().upper()
    
print final_word
