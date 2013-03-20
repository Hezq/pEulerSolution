# Problem description: http://projecteuler.net/problem=66
#
# __main__
# 1. generate a list, which consist square nums of (1, 10000)
#   we suppose the solution won't exceed 10000 here.
# 2. for D in range(2, 1001), solve quadratic Diophantine equation
#   for the minimal x value.
#
# solveQuadDioph
# 1. try x from 2 (xCand = 2)
# 2. for y in range(1, xCand), try if the quadratic Diophantine equation established.
#   return for True
# 3. increase xCand, goto 2

import math

def quadDiophValue(x, y, D):
    return x*x - D * y*y - 1

def isSquare(num):
    sq = int(math.sqrt(num))
    if sq * sq == num:
        return True
    return False

def solveQuadDioph(D):
    if isSquare(D):
        return (0, 0)
    xCand = 2
    while True:
        for yCand in [xCand-i for i in range(1, xCand)]:
            qDiophValue = quadDiophValue(xCand, yCand, D)
            if qDiophValue == 0:
                return (xCand, yCand)
            elif qDiophValue > 0:
                break
        xCand += 1
    return (0, 0)

if __name__ == '__main__':
##    for i in range(2, 14):
##        print solveQuadDioph(i)
    print solveQuadDioph(46)
    exit(0)
    minimalX = 0
    for i in range(2, 1001):
        result = solveQuadDioph(i)
        if 0 != result[0] and minimalX < result[0]:
            result = (result[0], result[1], i)
    print result
