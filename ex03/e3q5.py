"""
Exercise 3, question 5
This program is calculating the sum of the equation i/(i+1) for every i in the range i-n when n is given
and prints out the sum of each i until it get to n and print the final sum of the equation.
The function is using the recursion method.
"""


def m(n):
    func = lambda x: x / (x + 1)  # creates a lambda that will calculate the wanted equation

    def SUM(i):  # an inner function that sums the numbers and is used recursively
        if i == 0:
            return 0
        else:
            return SUM(i - 1) + func(i)  # a recursive call to the SUM function with the next i
    return SUM(n)  # returns the sum after the recursive process


def f():
    num = input("Enter a number: ")
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    for i in range(1, int(num) + 1):
        print(str(i) + ': ' + str(m(i)))
    print("In total the sum is: " + str(m(int(num))))
