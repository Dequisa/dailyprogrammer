#https://www.hackerrank.com/challenges/staircase
"""
Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?
"""

staircaseHeight = int(raw_input())

for a in xrange(0, staircaseHeight):
    currentRow = []
    for b in xrange(0,staircaseHeight-a-1):
        currentRow.append(' ')
    while len(currentRow) < staircaseHeight:
        currentRow.append('#')
    print ''.join(currentRow)

