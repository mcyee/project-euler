# Smallest Multiple

Smallest positive multiple evenly divisible by all numbers 1 through 20

## Thoughts

* 1, 2, 3, 5, 7, 11, 13, 17, 19 are prime
* 4 = 1, 2, 4
* 6 = 1, 2, 3, 6
* 8 = 1, 2, 4
* 9 = 1, 3, 9
* 10 = 1, 2, 5, 10
* 12 = 1, 2, 3, 4, 6, 12
* 14 = 1, 2, 7, 14
* 15 = 1, 3, 5, 15
* 16 = 1, 2, 4, 8, 16
* 18 = 1, 2, 3, 6, 9, 18
* 20 = 1, 2, 4, 5, 10, 20

* 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

## First Idea

* start from `n` = 20 and increment by 1 each time
* check if every number 11 through 20 divides `n` evenly (this also covers factors 1 through 10)
* if they all divide `n` evenly, then it is the smallest multiple

## Second Idea

* Find the gcd
* 11, 12, 13, 7, 5, 8, 17, 9, 19

## Third Idea

* get all prime factors
* 20 = 1, 2, 2, 5
* 18 = 1, 2, 3, 3
* 16 = 1, 2, 2, 2, 2
* 15 = 1, 3, 5
* 14 = 1, 2, 7
* 12 = 1, 2, 2, 3
* 10 = 1, 2, 5
* 9 = 1, 3, 3
* 8 = 1, 2, 2, 2
* 6 = 1, 2, 3
* 4 = 1, 2, 2
* 19, 17, 13, 11, 7, 5, 3, 2, 1

* 2 ^ 4
* 3 ^ 2
* 5, 7, 11, 13, 17, 19

* maximum number of each prime factor found in each of 1 through 20
  * get all prime factors for each number
    * use largest prime factor fn 
  * for each prime factor, get max count
