"""
Exercise 5, question 2
This program is using generators to execute the 'napa' function and using it to print a list of all the prime
dividers of the inserted N.
"""


def primeList(n):
    return [i for i in range(2, n + 1) if all([True if i % j != 0 else False for j in range(2, i - 1)])]


def primeFactors(N):
    pl = primeList(N)
    return (i for i in pl if N % 1 == 0)


