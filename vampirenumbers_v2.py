import itertools

fangs_num = input("How many fangs would you like? ")
#digits = input("How many digits would you like in the vampire number? ")

fangs_list = []
for x in range(10, 100):
	fangs_list.append(x)

possible_fangs = list(itertools.permutations(fangs_list, fangs_num))

final_fangs = []

def isfang(fangtocheck):
	fangsproduct = reduce(lambda x, y: x*y, fangtocheck)
	sorted_fangs = ""
	
	for a in range(0, len(fangtocheck)):
		sorted_fangs = sorted_fangs + (str(fangtocheck[a]))
	
	sorted_fangs = sorted(sorted_fangs)
	
	if sorted(list(str(fangsproduct))) == sorted_fangs and fangsproduct not in final_fangs:
		print "%d is a vampire number.  It's fangs are %s" %(fangsproduct, ','.join(str(a) for a in fangtocheck))
		final_fangs.append(fangsproduct)

for a in range(0, len(possible_fangs)):
	isfang(possible_fangs[a])







    
