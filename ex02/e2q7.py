"""
Exercise 2, question 7
This program is making a dictionary of twin prime numbers according to a given number.
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
    twins = []
    for i in range(len(x)):
        c = False
        for j in range(len(x)):
            if int(x[i]) == int((x[j] - 2)):
                twins.append(x[j])
                c = True
        if not c:
            twins.append("no twins")
    for i in range(len(twins)):
        twins[i] = str(twins[i])
    D = dict(zip(x, twins))
    return D


def f():
    num = input("Enter a positive number: ")
    primes = twinp(num)
    for keys, values in primes.items():
        print(str(keys) + ": " + str(values))

f()
