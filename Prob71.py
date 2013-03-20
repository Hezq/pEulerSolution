# Problem description: http://projecteuler.net/problem=71
#
# for each denominator D in pre-defined range:
#   1. find approximate nominator A = 3 * D / 7,
#        which means A/D <= 3 / 7
#   2. find qualified nominator NOM by try and decrease A for
#       there exists no common factor between NOM and D.
#   3. calculate DIFF = 3/7 - A/D, find minimal DIFF and get A as result.


def hasCommonFactor(a, b, primes):
# 'primes' is the prime number lists for acceleration
    if a == b:
        return True
    minV = min(a, b)
    for i in primes:
        if i > minV:
            break
        if a % i == 0 and b % i == 0:
            return True
    return False


def findNom(candNor, denom):
    while candNor > 0:
        if not hasCommonFactor(candNor, denom, primeList):
            break
        candNor -= 1
    return candNor

def genPrimeList(upperBound):
    primeMask = [1 for i in range(0, upperBound+1)]
    for i in range(2, upperBound/2+1):
        j = 2
        while i * j <= upperBound:
            primeMask[i * j] = 0
            j += 1
    primeList = []
    for i in range(2, upperBound+1):
        if primeMask[i] == 1:
            primeList.append(i)
    return primeList

if __name__ == '__main__':
#    primeList = genPrimeList(1000000)
    DIFF = 1
    RESULT = (0, 0)
    refPoint = float(3) / 7
    for i in range(1, 1000000+1):
        A = (3 * i) / 7
##        if hasCommonFactor(A, i, primeList):
##            continue
##        NOM = findNom(A, i)
        NOM = A
        if NOM != 0:
            currDiff = refPoint - float(NOM) / i
            if currDiff < DIFF and currDiff != 0:
                RESULT = (NOM, i)
                DIFF = currDiff
    print RESULT

