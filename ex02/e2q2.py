"""
Exercise 2, question 2
This program is getting a number and in two ways can calculate the sum of it's digits.
"""


def sumDigits1(num):
    num = int(num)
    sum = 0
    while num > 0:  # splits the number by digits (from right to left) and sums them
        reminder = num % 10
        sum += reminder
        num = num // 10
    return sum


def sumDigits2(num):
    number = [int(x) for x in str(num)]  # converts num from int to list of individual integers
    return sum(number)


def f():
    num = input("Enter a number: ")
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    SUM1 = sumDigits1(num)
    SUM2 = sumDigits2(num)
    print("The sum calculated by the first function is: " + str(SUM1))
    print("and the sum calculated by the second function is: " + str(SUM2))

f()
