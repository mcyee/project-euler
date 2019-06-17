################################################################################
# Project Euler
# Problem 5: Smallest Multiple
# Description: Find the smallest positive number that is evenly divisible by
#              numbers 1 through 20
################################################################################

from functools import reduce

PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19]
FACTORS = [5, 7, 9, 11, 13, 16, 17, 19]

def getSmallestMultiple():
    multiple = reduce((lambda x, y: x * y), PRIMES)
    # while True:
    #     if isDivisible(multiple):
    #         return multiple
    #     multiple = multiple + 1

def getLargestPrimeFactor(quotient):
    currentNum = 2
    while currentNum < quotient:
            if quotient % currentNum == 0:
                    quotient = quotient / currentNum
            currentNum = currentNum + 1
    return quotient

def getFactors(n):
    currentNum = n
    factorList = []
    while currentNum > 1:
        factor = getLargestPrimeFactor(n)
        factorList.append(factor)
        currentNum = currentNum / factor
    return factorList

def getProductOfFactors(factors):
    return reduce((lambda x, y: x * y), factors)

# print(getSmallestMultiple())
print(getProductOfFactors(FACTORS))
