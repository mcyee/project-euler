################################################################################
# Project Euler
# Problem 6: Sum Square Difference
# Description: Find the difference between the sum of the squares of the first
#              hundred natural numbers and the square of the sum
################################################################################

def getSumOfSquares(max):
    sum = 0
    for i in range(1, max + 1):
        sum = sum + (i ** 2)
    print("sum of squares: ", str(sum))
    return sum

def getSquareOfSum(max):
    sum = 0
    for i in range(1, max + 1):
        sum = sum + i
    print("square of sum: ", str(sum ** 2))
    return sum ** 2

def getDifference(max):
    return getSquareOfSum(max) - getSumOfSquares(max)

print(getDifference(100))
