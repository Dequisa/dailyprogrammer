import random
from random import shuffle


def word_scramble(word_in):
    word_array = list(word_in)
    if len(word_array) < 4:
       print(len(word_array))
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
       
       print new_array	   
       new_array  = random.shuffle(new_array)
       
       print word_array[0]
       print new_array
       print word_array[len(word_array)-1]
       
       new_array = [word_array[0]]+ new_array + [word_array[len(word_array)-1]]
       return ''.join(new_array)


input_word = raw_input("Give me a word: ")
#print(word_scramble(input_word))

a = [1,2,3,4]
print random.shuffle(a)