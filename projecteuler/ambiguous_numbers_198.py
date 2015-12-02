from __future__ import division

final_counter = 0
p = 1

def ambig_check(numerator, denominator, dbound):
    numer = 1
    denom = 1
    best_approx = 1
    for d in range (1, dbound + 1):
        for p in range(1, numerator + 1):
            if (abs((p/d) - ((numerator/denominator))) < abs(best_approx - ((numerator/denominator)))):
                best_approx = (p/d)
                numer = p
                denom = d

    for d in range (1, dbound + 1):
        for p in range(1, numerator + 1):
            if abs((p/d) - ((numerator/denominator))) == abs(best_approx - ((numerator/denominator))) and (p/d) != best_approx and p%d != numer/denom:
                print "The two fractions are %d/%d and %d/%d" %(p,d,numer,denom)
                return True
    return False

def check_ambiguity(numerator, denominator):
    num = float(numerator)/denominator 
    denom_start = 2
    min_error = 9000000
    for s in xrange(denom_start,denominator):
        for r in xrange(1,numerator+1):
            negative_error = num - float(r)/s
            if negative_error < 0:
                positive_error = num - float(r-1)/s
                if positive_error == min_error * -1:
                    print("%d/%d is an ambiguous number with %d/%d as one approximation" % (numerator, denominator, r-1, s))
                    return True
                elif positive_error < abs(min_error):
                    min_error = positive_error
                
                if negative_error == min_error * -1:
                    print("%d/%d is an ambiguous number with %d/%d as one approximation" % (numerator, denominator, r, s))
                    return True
                elif abs(negative_error) < abs(min_error):
                    min_error = negative_error
                else:
                    denom_start = r-1
                    break
    return False

for q in range(500, 800):
    p = 1
    while p/q < 1/100:
        for d in range(1, q):
           if ambig_check(p,q,d):
               final_counter += 1
           print "Currently looking at %d/%d with d_bound %d" %(p,q,d)
        p += 1

print final_counter


