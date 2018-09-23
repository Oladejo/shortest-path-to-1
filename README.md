# Description

I found a [nice post about dynamic programming on freecodecamp]( https://medium.freecodecamp.org/demystifying-dynamic-programming-24fbdb831d3a).

In that post, the author describes a problem and solves it using dynamic programming,
both 'top down' and 'bottom' up'.

It's a good read, you should read it.

I decided to implement it myself using a few different solutions

# The problem

Given an integer n, find the minimum number of steps to reach integer 1.

At each step, you can:
   *  Substract 1
   *  Divide by 2 (if it is divisible by 2)
   *  Divide by 3 (if it is divisible by 3)

     
# Solutions

I started by implementing this in 4 different ways:
1. brute-force: calculate all solutions, return the shortest
1. check-against-best-solution-so-far:
    * Like brute-force, but remembers the solution so far and stops calculating if the solution we're working on is already worse than the best so far. 
    * To optimize things this first calculates division by 3, then by 2 and only at the end
it does minus 1.
1. top-down dynamic programming
1. bottom-up dynamic programming


# Performance analysis


| n   | 200 | 2,000,000 | 200,000,000
| --- | --- | ---     | ---
| Bruteforce | 1.73s | n/a | n/a
| Check against best solution | 0.000055s | 0.075s | 8.06s
| Top down | 0.00023s | overflow | overflow 
| Bottom up | 0.00018s | 1.85s | n/a


This performed mostly as expected:
   * brute-force didn't scale
   * top down dynamic programming quickly had an overflow (due to the recursive implementation)
   * bottom up dynamic programming performed well
 
But the one unexpected result was that algoritm number 2 performed best **by far**

# Can we do better?

I was not satisfied with these results.
I would have expected the top down dynamic programming solution to scale better than 1000.

The problem was that it always calculated the 'always substract 1' solution,
which we **know** is not optimal anyway.


After giving that some thought I realized that dividing by 3 whenever possible
is always optimal, as it makes the biggest jump.
So I decided to reword the problem as:
   * Divide by 3 if possible
   * else calculate divide by 2 if possible and calculate minus 1

Implementing this gave me these new updated performance results:

| n   | 200 | 2,000,000 | 200,000,000 | 2,000,000,000,000,000 | 20,000,000,000,000,000 |
| --- | --- | ---     | ---       | ---              | ---
| Bruteforce | 1.73s | n/a | n/a  | n/a | n/a
| Check against best solution | 0.000055s | 0.075s | 8.06s | n/a | n/a
| Top down | 0.00023s | overflow | overflow | overflow | overflow
| Bottom up | 0.00018s | 1.85s | n/a | n/a | n/a
| Top down optimized algorithm | 0.000028s | 0.00015s |  0.00031s | 0.0011s |  overflow

Which gives us a clear winner.

# Lessons learned

 1. Don't assume a fancy solution like 'dynamic programming' is always best.
    * Sometimes a simple optimization like comparing with a known good solution might just be better.
 1. Look at your problem. See if you can reformulate it in a more efficient way




    