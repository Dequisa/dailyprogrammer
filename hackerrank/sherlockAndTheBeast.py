#https://www.hackerrank.com/challenges/sherlock-and-the-beast
#encoding=utf-8
"""
Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus; however, he also gives him a clue—a number, N. Sherlock determines the key to removing the virus is to find the largest Decent Number having N digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
If there are more than one such number, we pick the largest one.
"""

testCases = int(raw_input().strip())

def addFivesOrThrees(fivesNum, threesNum, digitNumber):
    possibleSolution = []
    if fivesNum==digitNumber:
        for five in xrange(0, fivesNum):
            possibleSolution.append('5')
        return possibleSolution
    if threesNum==digitNumber:
        for three in xrange(0, threesNum):
            possibleSolution.append('3')
        return possibleSolution
    else:
        for five in xrange(0, fivesNum):
            possibleSolution.append('5')
        for three in xrange(0, threesNum):
            possibleSolution.append('3')
        return possibleSolution

for a in xrange(0, testCases):
    digitNumber = int(raw_input().strip())
    possibleNumberOfThrees = []
    possibleNumberOfFives = []
    possibleSolutions = []
    biggestDecentNum = -1
    for b in xrange(1, digitNumber+1):
        if b%3==0:
            possibleNumberOfFives.append(b)
        if b%5==0:
            possibleNumberOfThrees.append(b)

    if possibleNumberOfFives == []:
        for threesNum in possibleNumberOfThrees:
            if threesNum == digitNumber:
                possibleSolutions.append(addFivesOrThrees(0, threesNum, digitNumber))

    if possibleNumberOfThrees == []:
        for fivesNum in possibleNumberOfFives:
            if fivesNum == digitNumber:
                possibleSolutions.append(addFivesOrThrees(fivesNum, 0, digitNumber))
                                       
    for threesNum in possibleNumberOfThrees:
        for fivesNum in possibleNumberOfFives:
            if threesNum+fivesNum==digitNumber or threesNum==digitNumber or fivesNum==digitNumber:
                possibleSolutions.append(addFivesOrThrees(fivesNum, threesNum, digitNumber))


    for solution in possibleSolutions:
        if int(''.join(solution)) > biggestDecentNum:
            biggestDecentNum = int(''.join(solution))
    print biggestDecentNum


"""
            if threesNum + fivesNum == digitNumber:
                possibleSolution = []
                for five in xrange(0, fivesNum):
                    possibleSolution.append('5')
                for three in xrange(0, threesNum):
                    possibleSolution.append('3')
                possibleSolutions.append(possibleSolution)

            if threesNum == digitNumber:
                possibleSolution = []
                for three in xrange(0, threesNum):
                    possibleSolution.append('3')
                possibleSolutions.append(possibleSolution)

            if fivesNum == digitNumber:
                possibleSolution = []
                for five in xrange(0, fivesNum):
                    possibleSolution.append('5')
                possibleSolutions.append(possibleSolution)
"""
