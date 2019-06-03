################################################################################
# Project Euler
# Problem 4: Largest Palindrome Product
# Description: Find the largest palindrome product of two 3-digit numbers
################################################################################

def getLargestPalindromeProduct(factor1, factor2):
    f1 = factor1
    f2 = factor2
    palindromeMax = -1

    while f1 > 100:
        while f2 > 100:
            product = f1 * f2
            if isPalindrome(product) and product > palindromeMax:
                palindromeMax = product
            f2 = f2 - 1
        f1 = f1 - 1
        f2 = f1
    return palindromeMax

def isPalindrome(x):
    stringVal = str(x)
    stringReverse = stringVal[::-1]
    for char1, char2 in zip(stringVal, stringReverse):
        if char1 != char2:
            return False
    return True

print(getLargestPalindromeProduct(999, 999))
