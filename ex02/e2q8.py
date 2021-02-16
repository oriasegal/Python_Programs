"""
Oria Segal 209338193
Exercise 2, question 8
This program is combining three dictionaries into one.
"""


def add3dict(d1, d2, d3):
    def val(d, key):
        # a func that will go through the dictionary and look if it has the d key and will return the value in this spot
        if key in d:  # if this key is in the dictionary
            return d[key]  # returns the value at this spot
        else:
            return None  # if it's not- returns None

    def values(key):
        # a func that combine all the values of the same key in all the dictionaries into one tuple
        t = tuple(filter(lambda x: x != None, (val(d1, key), val(d2, key), (val(d3, key)))))
        if len(t) == 1:  # as said in the question - if it's only one object it doesn't need to be a tuple
            return t[0]
        else:  # if it's more then one returns as a tuple
            return t
    k = set(d1) | set(d2) | set(d3)  # creates a list of all the keys of the three dictionaries
    v = map(values, k)  # creates a list of all the values of the three dictionaries
    return dict(zip(k, v))  # returns a dictionary of all the keys and each one has the values from all dictionaries


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

