"""
Exercise 2, question 6
This program is calculating the proximity value of pi by using a given number and the sum of the pi equation.
"""
import math


def l(n):
    s = lambda i: 4 * (math.pow(-1, (i + 1))) / (2 * i - 1)
    return [s(i) for i in range(1, int(n) + 1)]


def pi(n):
    pi = l(n)  # returns a list of the values of (-1)^(i+1)/(2i-1) for each i up to n
    # print(s)
    return sum(pi)  # returns the sum of the values in the list pi


def f():
    num = input("Enter a positive number: ")
    for i in range(1, int(num) + 1):
        print(str(i) + ': ' + str(pi(i)))
    print("The value of pi (according to n) is: " + str(pi(num)))

f()
