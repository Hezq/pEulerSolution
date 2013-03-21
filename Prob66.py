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

def yExistsForQd(x, D, y):
    ySqua = y * y
    quad = ySqua * D + 1
    if isSquare(quad):
        x[0] = int(math.sqrt(quad))
        return True
    return False

def solveQuadDioph(D):
    if isSquare(D):
        return (0, 0)
##    xCand = 2
    yCand = 1
    while True:
        xCand = [0]
        if yExistsForQd(xCand, D, yCand) == True:
            return (xCand[0], yCand)
        yCand += 1
    return (0, 0)

if __name__ == '__main__':
##    for i in range(2, 14):
##        print solveQuadDioph(i)
##    print solveQuadDioph(61)
##    exit(0)
    maximumX = 0
    for i in range(2, 1001):
        result = solveQuadDioph(i)
        print i, result
        if 0 != result[0] and maximumX < result[0]:
            maximumX = result[0]
            result = (result[0], result[1], i)
    print result
