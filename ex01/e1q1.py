"""
Exercise 1, question 1
This program is checking if three numbers are correct triangle sides length or not by comparing them to each other.
"""

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print("They are correct triangle sides lengths.")
else:
    print("They are in error.")


