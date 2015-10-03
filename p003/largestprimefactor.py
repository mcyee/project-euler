################################################################################
# Project Euler
# Problem 3: Largest Prime Factor
# Description: Find the largest prime factor of 600851475143
################################################################################

TERM = 600851475143
quotient = TERM

currentNum = 2
while currentNum < quotient:
	if quotient % currentNum == 0:
		quotient = quotient / currentNum
	currentNum = currentNum + 1

print(quotient)

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

###### ORIGINAL

# TERM = 600851475143
# currentNum = TERM
# divisible = False

# while (not divisible) and (currentNum > 1):

# 	print("currentNum is: " + str(currentNum))

# 	# check if currentNum divides TERM
# 	if TERM % currentNum == 0:

# 		print("currentNum divides evenly: " + str(currentNum))

# 		# check if currentNum is prime
# 		prime = True
# 		factor = currentNum - 1
# 		while prime and (factor > 1):
# 			if currentNum % factor == 0:
# 				prime = False
# 			factor = factor - 1

# 		print(str(currentNum) + " is prime: " + str(prime))

# 		# found prime factor
# 		if prime == True:
# 			divisible = True

# 	currentNum = currentNum - 1

# print(currentNum + 1)