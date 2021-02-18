"""
Exercise 1, question 6
This program is counting how many of each kind of data we enter in the list- how many lists, tuples, ints etc.
"""

List = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33, 0), ['d'], 'e']
print(List)
"""
OR:
List = eval(input("Enter a list with all kinds of objects "))

"""
L = sum(isinstance(i, list) for i in List)
I = sum(isinstance(i, int) for i in List)
F = sum(isinstance(i, float) for i in List)
S = sum(isinstance(i, str) for i in List)
T = sum(isinstance(i, tuple) for i in List)

total = list
D = dict(zip(['list', 'int', 'float', 'string', 'tuple'], [L, I, F, S, T]))
print(D)

