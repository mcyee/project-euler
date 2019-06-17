# Multiples of 3 and 5

Find the sum of all the multiples of 3 or 5 below 1000

## Solution 1 (brute force O(n))

* Start with `sum = 0`
* Iterate through all natural numbers `n` up to 1000
* If `n` is divisible (has remainder = 0) by 3 or 5, add to `sum`
