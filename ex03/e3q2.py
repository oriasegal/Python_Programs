"""
Exercise 3, question 2
This program is getting a number and in a recursive way can calculate the sum of it's digits.
"""


def sumDigits(n):
    n = int(n)
    if n == 0:
        return 0
    return (n % 10) + sumDigits(int(n / 10))


def f():
    num = input("Enter a number: ")
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    SUM = sumDigits(num)
    print("The sum calculated with a recursive function is: " + str(SUM))
