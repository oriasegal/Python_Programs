"""
Oria Segal, 209338193
Exercise 1, question 8
This program is
"""
"""import random

#r = random.randint(3, 9)
#print(r)

r = int(input("Enter N numbers in the range 3 - 9: "))

nums = []
for i in range(r):
    nums.append(random.randint(1, 9))
nums = tuple(nums)

print(nums)"""


#e1q5 - all functions as asked plus recursive (for the test)

def T(l):
    s = []
    for i in range(len(l)):
        if type(l[i]) == tuple:
            s = s + list(l[i])
    return s


def RT(l):
    if l == []:
        return []
    else:
        if type(l[-1]) == tuple:
            return RT(l[:-1]) + list(l[-1])
        else:
            return RT(l[:-1])


def L(l):
    s = ()
    for i in range(len(l)):
        if type(l[i]) == list:
            s = s + tuple(l[i])
    return s


def RL(l):
    if l == []:
        return ()
    else:
        if type(l[-1]) == list:
            return RL(l[:-1]) + tuple(l[-1])
        else:
            return RL(l[:-1])


def S(l):
    s = []
    for i in range(len(l)):
        if type(l[i]) == str:
            s = s + list(l[i])
    return s


def RS(l):
    if l == []:
        return []
    else:
        if type(l[-1]) == str:
            return RS(l[:-1]) + list(l[-1])
        else:
            return RS(l[:-1])


def N(l):
    s = []
    for i in range(len(l)):
        if isinstance(l[i], (int, float)):
            s = s + [l[i]]
    return s


def RN(l):
    if l == []:
        return []
    else:
        if isinstance(l[-1], (int, float)):
            return RN(l[:-1]) + [l[-1]]
        else:
            return RN(l[:-1])


print(N([1, 2, 'a', (11,2,'b'), [22,'c'], (33,), ['d'], 'e']))
print(RN([1, 2, 'a', (11,2,'b'), [22,'c'], (33,), ['d'], 'e']))
