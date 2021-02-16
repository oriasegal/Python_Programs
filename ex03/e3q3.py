"""
Oria Segal 209338193
Exercise 3, question 3
This program is printing out the number that is given in reverse by using a recursive function.
"""


def reverseNum(num):
    if num == "":
        return num  # when gets to the end of the number returns the num
    else:
        return reverseNum(num[1:]) + num[0]  # a recursive call to the func with the number starting one digit off
        # from the left side (293 will get sent as 93)


def f():
    num = input("Enter a number: ")
    if num[0] == '-':
        num = num[1:]
    reverse = reverseNum(num)
    print("The sum calculated by the recursive function is: " + str(reverse))

