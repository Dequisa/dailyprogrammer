def isPalindrome(n): 
    reg_n = list(str(n))
    rev_n = list(str(n))
    rev_n.reverse()

    if int(''.join(reg_n)) == int(''.join(rev_n)):
        return True
    else:
        return False

biggest = 0

for x in range(100,999):
    for y in range(100,999):
        if isPalindrome(x*y) and x*y > biggest:
            biggest = x*y
            print biggest




