import random
from random import shuffle

def word_scramble(word_in):
    word_array = list(word_in)
    if len(word_array) < 4:
       return word_in

    elif len(word_array) == 4:
       store_letter = word_array[1]
       word_array[1]=word_array[2]
       word_array[2]=store_letter
       return ''.join(word_array)

    elif len(word_array) > 4:
       new_array = range(len(word_array)-2)
      
       for x in range(0, len(word_array)-2):
	   new_array[x] = word_array[x+1]
       
       new_array  = sorted(new_array, key=lambda k:random.random())
       
       
       new_array = [word_array[0]]+ new_array + [word_array[len(word_array)-1]]
       return ''.join(new_array)


input_text = raw_input("Give me some text: ")

input_list = input_text.split()

output_list = range(0, len(input_list))

for x in range(0, len(input_list)):

    output_list[x] = (word_scramble(input_list[x]))

print ' '.join(output_list)
