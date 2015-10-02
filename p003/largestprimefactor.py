################################################################################
# Project Euler
# Problem 3: Largest Prime Factor
# Description: Find the largest prime factor of 600851475143
################################################################################

TERM = 600851475143
currentNum = TERM
divisible = False

while (not divisible) and (currentNum > 1):

	print("currentNum is: " + str(currentNum))

	# check if currentNum divides TERM
	if TERM % currentNum == 0:

		print("currentNum divides evenly: " + str(currentNum))

		# check if currentNum is prime
		prime = True
		factor = currentNum - 1
		while prime and (factor > 1):
			if currentNum % factor == 0:
				prime = False
			factor = factor - 1

		print(str(currentNum) + " is prime: " + str(prime))

		# found prime factor
		if prime == True:
			divisible = True

	currentNum = currentNum - 1

print(currentNum + 1)