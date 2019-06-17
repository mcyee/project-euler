# Largest Prime Factor

Find the largest prime factor of the given number.

## Fourth Algorithm (Solution)

Start at 2, and increment by one.  
Let `quotient` be `n` and divide it as many times as possible by the current number.  
When the current number is `quotient`, stop. `quotient` is the largest prime factor.

## Thoughts

* Is there a way to skip numbers the bigger the factor becomes, to shorten the list of factors/testing for divisibility?

## Third Idea

Generate prime numbers from 2, and continue until `n`.  
Check if the prime divides evenly into `n`.  
If it does, append it to a list of all prime factors of `n`.  
The last element in the list is the largest prime factor.

## Second Algorithm

Start from `n` itself and decrement by one each time.  
Check if the number divides `n` evenly (number is a factor of `n`).  
In descending order, check if the factor is divisible by the smaller factors of `n`.  
If it isn't divisible by any of them, then it is the largest prime factor.

## Original Algorithm

Start from `n` itself and decrement by one each time.  
Check if the number divides `n` evenly (number is a factor of `n`).  
If it does, check if it is prime.  
If it is prime, then it is the largest prime factor.
