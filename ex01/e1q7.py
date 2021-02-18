"""
Exercise 1, question 8
This program is getting a random text and reads is while counting how many times each word is mentioned in it.
Prints out the results in a dictionary form.
"""

import string

text = open("shakespeare.txt" , "r")
d = dict()

for line in text:
    line = line.strip() # for spaces and newlines in the text
    line = line.lower() # makes sure all is in lowercase letters
    line = line.translate(line.maketrans("", "", string.punctuation)) # remove the punctuation marks from the line
    words = line.split(" ") # splits the line into words

    for word in words:
        if word in d: # check if the word is already in dictionary
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()): # prints the contents of dictionary
    print(key, ":", d[key])

