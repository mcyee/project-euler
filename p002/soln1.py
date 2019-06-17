################################################################################
# Project Euler
# Problem 2: Even Fibonacci Numbers
# Description: Sums all the even terms in the Fibbonacci sequence below 4000000
################################################################################

sum = 0
previousTerm = 1
currentTerm = 2

while currentTerm <= 4000000:
	# add term to sum
	if currentTerm % 2 == 0:
		sum = sum + currentTerm

	# generate next term
	nextTerm = previousTerm + currentTerm
	previousTerm = currentTerm
	currentTerm = nextTerm

print(sum)