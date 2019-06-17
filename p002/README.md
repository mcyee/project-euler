# Even Fibonacci Numbers

Find the sum of the even-valued terms in the Fibonacci sequence under 4 000 000

## Solution 1 (brute force O(n))

* Start with `sum = 0`
* Calculate the Fibonacci sequence with value under 4 000 000
* If current term `n` is divisible by 2, then add `n` to `sum`
