

pope_catholic = True

def mkstartingnum():
    while pope_catholic:
    	  user_input = input('Give me an integer greater than 0: ')
    	  
	  if isinstance(user_input, float):
       	     print('I said I needed an integer, not a float!')

    	  elif user_input < 1:
       	     print('make it bigger than 0 next time')

	  elif user_input > 0:
    	     return user_input
	     break

def mktotal(in_number):
    total = 0
    start_array = list(str(in_number))
    for x in range(0,len(start_array)):
    	start_array[x]=int(start_array[x])
    	total = start_array[x] + total
    return total

start_number = mkstartingnum()

mktotal(start_number)

while pope_catholic:
      if start_number == 1:
      	 print('all done!')
	 break

      if start_number < 0:
         print('this shouldnt happen')
	 break

      elif mktotal(start_number)%3 == 0:
      	 print(start_number, 0)
    	 start_number = start_number/3
    	 print(start_number)

      elif mktotal(start_number)%3 == 1:
      	 print(start_number, '-1')
    	 start_number = (start_number - 1)/3
    	 print(start_number)  

      elif mktotal(start_number)%3 == 2:
      	 print(start_number, '+1') 
    	 start_number = (start_number + 1)/3 
    	 print(start_number)



