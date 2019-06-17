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

# TERM = 600851475143
# factors = []

# # get factors of TERM
# for i in range(1, TERM):
# 	if TERM % i == 0 and i != 1:
# 		factors.append(i)
# 		print(i)

# print("list of factors:")
# for fact in factors:
# 	print(fact)

# # check if factor is divisible by smaller factors
# elem = len(factors) - 1
# while elem > 0:

# 	j = 0
# 	while j < elem:

# 		print("factors[elem]: " + str(factors[elem]))
# 		print("factors[j]: " + str(factors[j]))

# 		if factors[elem] != factors[j]:
# 			if factors[elem] % factors[j] == 0:
# 				popped = factors.pop(elem)
# 				print("popping " + str(popped))
# 				elem = elem - 1
# 				j = 0
# 		j = j + 1

# 	elem = elem - 1

# print(factors.pop())

