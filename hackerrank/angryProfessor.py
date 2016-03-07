#https://www.hackerrank.com/challenges/angry-professor
"""
A Discrete Mathematics professor has a class of NN students. Frustrated with their lack of discipline, he decides to cancel class if fewer than KK students are present when class starts.
"""

testCaseNum = int(raw_input().strip())

for x in xrange(0, testCaseNum):
    lineInfo = map(int, raw_input().split(' '))
    onTime = 0
    threshhold = lineInfo[1]
    arrivalTimes = map(int, raw_input().split(' '))
    for arrivalTime in arrivalTimes:
        if arrivalTime < 1:
            onTime += 1
    if onTime >= threshhold:
        print 'NO'
    else:
        print 'YES'
