"""
Exercise 4, question 3
This program is getting a list of lists from the user and by using recursive functions can sort them or print
them in reverse.
"""


def bubblesort(l):
    def bubblesortrec(l, i, j, n):
        if j == n:
            i = i + 1
            j = 0
        if i == n:
            return
        if l[i] < l[j]:
            temp = l[j]
            l[j] = l[i]
            l[i] = temp

            bubblesortrec(l, i, j + 1, n)
        else:
            bubblesortrec(l, i, j + 1, n)

        return l

    l = bubblesortrec(l, 0, 0, len(l))
    return l


def sortedzip(l):
    s = []

    def sortedziprec(i, l, s):
        if i == len(l):
            return s
        else:
            s.append(bubblesort(l[i]))
            return sortedziprec(i + 1, l, s)

    s = sortedziprec(0, l, [])
    zippedS = list(zip(*s))
    return zippedS


def reverse(l):
    return l[::-1]


def reversedzip(l):
    s = []

    def reversedziprec(i, l, s):
        if i == len(l):
            return s
        else:
            s.append(reverse(l[i]))
            return reversedziprec(i + 1, l, s)

    s = reversedziprec(0, l, [])
    reversedS = list(zip(*s))
    return reversedS


def funczip(func, l):
    if func == sortedzip:
        print("The original list is:")
        print(l)
        zippedL = sortedzip(l)
        print("The sorted and zipped list is:")
        print(zippedL)

        return

    if func == reversedzip:
        print("The original list is:")
        print(l)
        reversedL = reversedzip(l)
        print("The reversed and zipped list is:")
        print(reversedL)

        return


l = eval(input("Enter a list of lists: "))
functions = {'sortedzip': sortedzip, 'reversedzip': reversedzip}
f = input("Enter the function you want to operate on your list\nTo sort and zip enter sortedzip\nTo reverse and zip enter reversedzip\n")
func = functions[f]
funczip(func, l)
print(l)


# l = [['c', 'b', 'a', 'z'], [5, 6, 10, 1], [20, 19, 18, 17]]
