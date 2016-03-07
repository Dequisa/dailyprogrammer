#https://www.hackerrank.com/challenges/time-conversion
"""
Given a time in AM/PM format, convert it to military (24-hour) time.
"""

startTime = list(raw_input().strip())

if startTime[8] == 'A':
    if int(''.join(startTime[0:2])) == 12:
        print '00' + ''.join(startTime[2:8])
    else:
        print ''.join(startTime[0:8])

if startTime[8] == 'P':
    if int(''.join(startTime[0:2])) == 12:
        print ''.join(startTime[0:2]) + ''.join(startTime[2:8])
    else:
        print str(int(''.join(startTime[0:2])) + 12) + ''.join(startTime[2:8])
