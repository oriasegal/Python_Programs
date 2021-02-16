"""
Oria Segal 209338193
Exercise 3, question 4
This program is checking if the number that was given is a palindrome or not and prints out the matching message.
"""


def isPolindrome(num):
    if num[0] == '-':  # if it's a negative number it cuts the sigh out
        num = num[1:]
    if num == num[::-1]:
        return True
    else:
        return False


def f():
    num = input("Enter a number: ")
    N = isPolindrome(num)
    if N:
        print("It is a palindrome!!")
    else:
        print("It is not a palindrome.")
