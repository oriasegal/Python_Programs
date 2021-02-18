"""
Exercise 3, question 6
This program is calculating the proximity value of pi by using a given number and the sum of the pi equation.
The value is calculated using a recursive function.
"""
import math


def pi(n):
    func = lambda i: 4 * (math.pow(-1, (i + 1))) / (2 * i - 1)

    def SUM(i):  # an inner function that sums the numbers and is used recursively
        if i == 0:
            return 0
        else:
            return SUM(i - 1) + func(i)  # a recursive call to the SUM function with the next i
    return SUM(n)  # returns the sum after the recursive process


def f():
    num = input("Enter a positive number: ")
    for i in range(1, int(num) + 1):
        print(str(i) + ': ' + str(pi(i)))
    print("The value of pi (according to n) is: " + str(pi(int(num))))
