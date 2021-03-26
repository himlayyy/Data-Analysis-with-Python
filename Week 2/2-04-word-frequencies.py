#!usr/bin/env python 3
""""
Create function word_frequencies that gets a filename as a parameter and returns a dict with the word frequencies. In 
the dictionary the keys are the words and the corresponding values are the number of times that word occurred in the 
file specified by the function parameter. Read all the lines from the file and split the lines into words using the 
split() method. Further, remove punctuation from the ends of words using the strip
method call.

Test this function in the main function using the file alice.txt. In the output, there should be a word and its count 
per line separated by a tab:

The     64
Project 83
Gutenberg   26
EBook   3
"""
from collections import defaultdict
import string
import re


def word_frequencies(filename):
    with open(filename) as f:
        text = f.readlines()
    word_frequency = defaultdict(int)
    for line in text:
        words = line.split()
        for word in words:
            clean_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            word_frequency[clean_word] += 1
    return dict(word_frequency)


frequency = word_frequencies(r"alice.txt")
print(len(frequency))
for key, value in frequency.items():
    print(f"{key}\t{value}", end="\n")
print(frequency["creating"], frequency["Carroll"],  frequency["sleepy"], frequency["Rabbit"])

