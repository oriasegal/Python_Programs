"""
Oria Segal 209338193
Exercise 3, question 1
This program is calculating the penta numbers in the range of two given numbers by using two recursive functions.
"""


def pentaNumRange(n1, n2):
    getPentaNum = lambda n: n * (3 * n - 1) / 2
    l = []

    def pentaRecu(n1, n2):
        if n1 == n2:
            return l
        else:
            l.append(str(getPentaNum(n1)) + " ")
            return pentaRecu(n1 + 1, n2)
    return pentaRecu(n1, n2)


def goDownLines(R):
    l = []

    def recu(R, i, l):
        if i == len(R) - 1:
            l.append(str(R[i]))
            return l
        else:
            if (i % 10) == 0:
                l.append('\n' + str(R[i]))
                return recu(R, i + 1, l)
            else:
                l.append(str(R[i]))
                return recu(R, i + 1, l)

    newR = recu(R, 0, l)
    return newR


def f():
    n1 = int(input("Enter your n1: "))
    n2 = int(input("Enter your n2: "))
    R = pentaNumRange(n1, n2)
    newR = goDownLines(R)
    print(" ".join(newR))
