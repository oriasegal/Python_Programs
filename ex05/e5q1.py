"""
Oria Segal 209338193
Exercise 5, question 1
This program is using generators to get all the even numbers between N1 and N2 and prints N3 in a row.
"""


def genEven(N1, N2):
    if N1 % 2 == 0:
        start = N1
    else:
        start = N1 + 1
    return (i for i in range(start, N2, 2))


def evenprt(N1, N2, N3):
    def helper(currGen, N3, counter):
        nextElem = next(currGen, None)
        if nextElem:
            print(nextElem, end = " ")
            if counter % N3 == N3 - 1:
                print()
            helper(currGen, N3, counter + 1)

    helper(genEven(N1, N2 + 1), N3, 0)


