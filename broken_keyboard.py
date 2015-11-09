all_working_words = []

working_keys = ''

final_list = []

total_inputs = raw_input("Enter how many keyboard configurations you will give me: ")

def isallowed(testword,ok_keys):
    letter_list = list(testword)
    for letter in letter_list:
        if letter not in ok_keys:
            return False
    return True

def getlongestword(working_keys):
    
    all_working_words = []

    with open("/usr/share/dict/words") as dictionary:

        for word in dictionary:
            if isallowed(word.strip(),working_keys):
                all_working_words.append(word.strip())

            all_working_words.sort(key=len, reverse=True)
        
        return all_working_words[0]

for x in range(int(total_inputs)):
    
    input_keys = raw_input("Enter the keys you have that still work: ")
    final_list.append('%s  =  %s' %(input_keys,getlongestword(input_keys)))

for item in final_list:
    print item
