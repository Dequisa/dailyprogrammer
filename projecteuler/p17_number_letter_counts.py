onesPlaceSize = {'0':0, '1': 3, '2':3, '3': 5, '4':4, '5':4, '6': 3, '7':5, '8':5, '9':4}
tensPlaceSize = {'0':0, '2': 6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
hundredsPlaceSize = {'0':0, '1': 13, '2':13, '3':15, '4':14, '5':14, '6':13, '7':15, '8':15, '9':14}

oneInTensPlaceSize = {'0':3, '1':6, '2':6, '3':8, '4':8, '5':7, '6':7, '7':9, '8':8, '9':8}

total = 0

def fitToSize(numberList):
    while len(numberList) != 3:
        numberList = ['0'] + numberList
    return numberList


def getSize(number):
    size = 0
    numberList = list(str(number))
    threeDigitList = fitToSize(numberList)
    size += hundredsPlaceSize[threeDigitList[0]]
    if threeDigitList[1] != '1':
        size += onesPlaceSize[threeDigitList[2]]
        size += tensPlaceSize[threeDigitList[1]]
    elif threeDigitList[1] == '1':
        size += oneInTensPlaceSize[threeDigitList[2]]

    #Corrects for the HashMap adding 'and' for each hundred

    if threeDigitList[0] != '0' and threeDigitList[1] == '0' and threeDigitList[2] == '0':
        size = size -3

    return size
  
for x in range(1,1000):
    total += getSize(x)

print total

