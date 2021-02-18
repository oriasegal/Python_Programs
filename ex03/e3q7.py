"""
Exercise 3, question 7
This program is making a dictionary of twin prime numbers according to a given number by using recursive functions.
"""


def napa(n):
    prime = [True] * n
    prime[0] = False
    for i in range(2, n):
        if prime[i]:
            for mlt in range(i * 2, n, i):
                prime[mlt] = False
    r = []
    for i, item in enumerate(prime):
        if item:
            r.append(i)
    return r


def twinp(n):
    x = napa(int(n))

    def tpRec(twins, i, x):
        if i == len(x):
            return twins
        else:
            if x[i] + 2 in x:
                twins.append(str(x[i] + 2))
                return tpRec(twins, i + 1, x)
            else:
                twins.append(False)
                return tpRec(twins, i + 1, x)

    twins = tpRec([], 0, x)

    for i in range(len(twins)):
        if not twins[i]:
            twins[i] = 'no twin'
    D = dict(zip(x, twins))
    return D


def f():
    num = input("Enter a positive number: ")
    primes = twinp(num)
    for keys, values in primes.items():
        print(str(keys) + ": " + str(values))
