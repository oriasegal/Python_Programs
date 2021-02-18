"""
Exercise 1, question 4
In this program there are four functions that are getting a binary word and can move N bits left or right
by putting '0' or '1' instead.
"""
import string

N = int(input("Enter a decimal number: "))
binNr = str(input("Enter a binary number: "))
print(N)
print(binNr)


def shiftL(s, n):
    a = binNr[n:]
    b = "0" * n
    return a + b


def shiftR(s, n):
    a = binNr[:-n]
    b = "0" * n
    return b + a


def shiftCL(s, n):
    a = binNr[:n]
    b = binNr[n:]
    return b + a


def shiftCR(s, n):
    a = binNr[-n:]
    b = binNr[:-n]
    return a + b


p = shiftL(binNr, N)
print(p)
p = shiftR(binNr, N)
print(p)
p = shiftCL(binNr, N)
print(p)
p = shiftCR(binNr, N)
print(p)
