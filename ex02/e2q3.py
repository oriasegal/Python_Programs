"""
Oria Segal 209338193
Exercise 2, question 3
This program is printing out the number that is given in reverse in two ways.
"""


def reverseNum1(num):
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    return str(num)[::-1]


def reverseNum2(num):
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    num = [int(x) for x in str(num)]  # turns num from a string into a list
    number = list(reversed(num))  # uses the reverse function
    number = [str(i) for i in number]  # turns number from a list into an int
    number = int("".join(number))  # connects the ints into a big int
    return number


def f():
    num = input("Enter a number: ")
    reverse1 = reverseNum1(num)
    reverse2 = reverseNum2(num)
    print("The sum calculated by the first function is: " + str(reverse1))
    print("and the sum calculated by the second function is: " + str(reverse2))


def solution(A):
    i = 1
    while(1):
        if i not in A:
            return i
        i = i + 1

#print(solution([1,2,3]))

import pandas as pd


def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')
    biopics.columns
    return biopics.reset_index(drop=True)