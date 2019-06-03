# Largest Palindrome Product

Find the largest palindrome product of two 3-digit numbers

## First Idea

* Start from the largest 3-digit number (999) and decrement one by one each time
* Check if the product is a palindrome
* If it is, then it is the largest palindrome product
* Once one factor is 100, decrement the other by one and start again with both factors (eg. at 998)
