"""
Exercise 2, question 5
This program is calculating the sum of the equation i/(i+1) for every i in the range i-n when n is given
and prints out the sum of each i until it get to n and print the final sum of the equation.
"""


def l(n):
    s = lambda i: i / (i + 1)
    return [s(i) for i in range(1, int(n) + 1)]


def m(n):
    s = l(n)  # returns a list of the values of i/(i+1) for each i up to n
    # print(s)
    return sum(s)  # returns the sum of the values in the list s


def f():
    num = input("Enter a number: ")
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    for i in range(1, int(num) + 1):
        print(str(i) + ': ' + str(m(i)))
    print("In total the sum is: " + str(m(num)))

f()
