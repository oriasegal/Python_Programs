"""
Oria Segal 209338193
Exercise 2, question 9
This is a program that calls all the other functions that were builds in the last 8 files
according to what the user requests.
"""
import math
import e2q1
import e2q2
import e2q3
import e2q4
import e2q5
import e2q6
import e2q7
import e2q8


def one():  # calls the f function in the e2q1 file
    e2q1.f()


def two():  # calls the f function in the e2q2 file
    e2q2.f()


def three():  # calls the f function in the e2q3 file
    e2q3.f()


def four():  # calls the f function in the e2q4 file
    e2q4.f()


def five():  # calls the f function in the e2q5 file
    e2q5.f()


def six():  # calls the f function in the e2q6 file
    e2q6.f()


def seven():  # calls the f function in the e2q7 file
    e2q7.f()


def eight():  # calls the f function in the e2q8 file
    e2q8.f()


print("To calculate penta numbers - enter 1")
print("To calculate the sum of your number's digits by using two functions - enter 2")
print("To get your number printed in revers by using two functions - enter 3")
print("To check if your number is a palindrome - enter 4")
print("To calculate the equation i/(i+1) - enter 5")
print("To calculate the proximity value of pi - enter 6")
print("To create a dictionary of twin prime numbers - enter 7")
print("To combine three dictionaries into one - enter 8")
print("To exit the program - enter 0")

num = 1
switcher = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 0: exit}
if num:
    while num:
        num = int(input("your choice: "))
        func = switcher.get(num, lambda: "Invalid number")
        print(func())
else:
    func = switcher.get(num, lambda: "Invalid number")

