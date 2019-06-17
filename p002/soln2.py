################################################################################
# Project Euler
# Problem 2: Even Fibonacci Numbers
# Description: Sums all the even terms in the Fibbonacci sequence below 4000000
################################################################################

import math

PHI = (1 + math.sqrt(5)) / 2
MAX_TERM_VALUE = 4000000

def getFibonacciTerm(n):
    return math.floor((PHI**n / math.sqrt(5)) + (1 / 2))

def getEvenTerms():
    sumOfEvens = 0
    i = 3
    value = 0
    while value <= MAX_TERM_VALUE:
        sumOfEvens = sumOfEvens + value
        value = getFibonacciTerm(i)
        i = i + 3
    return sumOfEvens

print(getEvenTerms())
