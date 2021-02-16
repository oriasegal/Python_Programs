"""
Oria Segal 209338193
Exercise 2, question 1
This program is calculating the penta numbers in the range of two given numbers.
"""
"""

def pentaNumRange(n1, n2):
    getPentaNum = lambda n: n * (3 * n - 1) / 2
    return [getPentaNum(n) for n in range(n1, n2)]


def string(i, val):
    if (i % 10) == 0:
        return '\n' + str(val)
    else:
        return str(val)


def f():
    n1 = int(input("Enter your n1: "))
    n2 = int(input("Enter your n2: "))
    R = pentaNumRange(n1, n2)
    print(R)
    newR = [string(i, val) for i, val in (enumerate(R))]
    print(newR)
    print(" ".join(newR))

f()

"""


def basecomp(base, s):
    counter = 0
    for i in range(len(s)):
        if s[i] == base:
            counter += 1
    p = (100/len(s))*counter
    return base, (counter, p)


def basecount(base,s):
    list = [basecomp(x,s) for x in base]
    return dict(map(lambda x: basecomp(x,s), base))


def f(s1,s2):
    T = list(zip(s1,s2))
    print(T)
    def help(L):
        if L == []:
            return ""
        else:
            if L[0][0] == L[0][1]:
                return L[0][0] + help(L[1:])
            else:
                return "-" + help(L[1:])
    return help(T)


print(f("actggctagc", "acttgctcgc"))
