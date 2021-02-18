"""
Exercise 3, question 8
This program is combining three dictionaries into one by using a 'tail recursion' styled function.
"""
# from tailrecurse import *


# @tail_call_optimized
def add3dict(d1, d2, d3):
    def recAddingDicts(k1, d1, k2, d2, k3, d3, totalKeys, totalVaues):
        if k1 == [] and k2 == [] and k3 == []:
            return dict(zip(totalKeys, totalVaues))

        elif k1 == [] and k2 == []:
            if k3[0] in d1 or k3[0] in d2:
                return recAddingDicts(k1, d1, k2, d2, k3[1:], d3, totalKeys, totalVaues)
            else:
                return recAddingDicts(k1, d1, k2, d2, k3[1:], d3, totalKeys + [k3[0]], totalVaues + [d3[k3[0]]])

        elif k1 == []:
            currKey = k2[0]
            if currKey in d1:
                return recAddingDicts(k1, d1, k2[1:], d2, k3, d3, totalKeys, totalVaues)
            elif currKey in d3:
                return recAddingDicts(k1, d1, k2[1:], d2, k3, d3, totalKeys + [currKey], totalVaues + [(d2[currKey], d3[currKey])])
            else:  # key is only in k2
                return recAddingDicts(k1, d1, k2[1:], d2, k3, d3, totalKeys + [currKey], totalVaues + [d2[currKey]])

        else:  # k1 is not empty
            currKey = k1[0]
            if currKey in d2 and currKey in d3:
                return recAddingDicts(k1[1:], d1, k2, d2, k3, d3, totalKeys + [currKey], totalVaues + [(d1[currKey], d2[currKey], d3[currKey])])
            elif currKey in d2:
                return recAddingDicts(k1[1:], d1, k2, d2, k3, d3, totalKeys + [currKey], totalVaues + [(d1[currKey], d2[currKey])])
            elif currKey in d3:
                return recAddingDicts(k1[1:], d1, k2, d2, k3, d3, totalKeys + [currKey], totalVaues + [(d1[currKey], d3[currKey])])
            else:  # key is only in k1
                return recAddingDicts(k1[1:], d1, k2, d2, k3, d3, totalKeys + [currKey], totalVaues + [d1[currKey]])

    d123 = recAddingDicts(list(d1.keys()), d1, list(d2.keys()), d2, list(d3.keys()), d3, [], [])
    return d123


def f():
    d1 = dict()
    d2 = dict()
    d3 = dict()
    user_input1 = input("Enter your first dictionary, key and value separated by commas (,): ")
    while user_input1 != 'done':
        key, value = user_input1.split(",")
        d1[key] = value
        user_input1 = input("Next value, key and value separated by commas (,): ")

    user_input2 = input("Enter your second dictionary, key and value separated by commas (,): ")
    while user_input2 != 'done':
        key, value = user_input2.split(",")
        d2[key] = value
        user_input2 = input("Next value, key and value separated by commas (,): ")

    user_input3 = input("Enter your third dictionary, key and value separated by commas (,): ")
    while user_input3 != 'done':
        key, value = user_input3.split(",")
        d3[key] = value
        user_input3 = input("Next value, key and value separated by commas (,): ")

    print(add3dict(d1, d2, d3))
