"""
Exercise 4, question 4
This program is creating an N lines long poem by using two recursive functions.
"""
import random

objects = ("Roni ", "Max ", "A chair ", "A bottle ")
verbs = ("eats ", "plays ", "buys ", "opens ")
adverbs = ("slowly ", "tomorrow ", "now ", "soon ", "suddenly ")
adjectives = ("tall ", "small ", "big ", "red ", "blue ")
animateObjects = ("oranges", "friends", "lake", "food", "trees")


def crPoem(N):
    # a function that creates a poem by using a recursive sub- function
    l = []

    def cp(N, l):
        # a recursive sub- function that creates a poem (a tuple of strings)
        # by choosing a random sentence from global options
        if N == 0:
            return l
        else:
            obj = str(random.choice(objects))
            verb = str(random.choice(verbs))
            adverb = str(random.choice(adverbs))
            adj = str(random.choice(adjectives))
            aniObj = str(random.choice(animateObjects))

            l.append(obj + verb + adverb + adj + aniObj)

            return cp(N - 1, l)

    poem = tuple(cp(N, l))
    return poem


def theHumbletPoet():
    # a function that is asking for a positive number, checks if it's correct
    # and uses a recursive sub- function to print the poem
    N = int(input("Enter the number of lines for your poem: "))

    while N < 0:  # checks if the value entered is correct
        print("The value entered is incorrect. Please enter a new value.")
        N = int(input())

    poem = crPoem(N)  # calls the recursive function to create a poem

    def printPoem(poem):
        # prints the poem recursively
        if len(poem) == 0:
            return
        else:
            r = list(poem)
            print(r.pop(0))
            return printPoem(r)

    printPoem(poem)

theHumbletPoet()
