import itertools
import time

startTime = time.clock()

for idx, item in enumerate(itertools.permutations(range(0,10))):
    if idx == 999999:   
        endTime = time.clock()
        print item, endTime - startTime


