# Even Fibonacci Numbers

Find the sum of the even-valued terms in the Fibonacci sequence under 4 000 000

## Solution 1 (brute force O(n))

* Start with `sum = 0`
* Calculate the Fibonacci sequence with value under 4 000 000
* If current term `n` is divisible by 2, then add `n` to `sum`

## Solution 2 (calculate only even terms)

Find a pattern to the even terms:

1 1 2 3 5 8 13 21 34 55 89 144

2 8 34 144 -- every third term

Is there a way to calculate every third term instead of all of them?

Use [**Binet's formula**](https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula):

F_n = floor(phi^n / sqrt(5) + 1/2) where n >= 0, phi = (1  + sqrt(5))/2

* Calculate every third term with Binet's formula and sum
