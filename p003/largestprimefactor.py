################################################################################
# Project Euler
# Problem 3: Largest Prime Factor
# Description: Find the largest prime factor of 600851475143
################################################################################

TERM = 600851475143

def getLargestPrimeFactor(quotient):
    currentNum = 2
    while currentNum < quotient:
            if quotient % currentNum == 0:
                    quotient = quotient / currentNum
            currentNum = currentNum + 1
    return quotient

print(getLargestPrimeFactor(TERM))
