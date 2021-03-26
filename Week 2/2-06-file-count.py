#!usr/bin/env python3
"""
Create a function file_count that gets a filename as parameter and return a triple of numbers. The function should read
the file, count the number of lines, words, and characters in the file, and return a triple with these count in this
order. You get division into words by splitting at whitespace, you don't have to remove punctuation.

Part 2.

Create a main function that calls file_count for each filename in the list of command line parameters sys.argv[1:].
For call python3 src/file_count file1 file2 ... the output should be
?      ?       ?       file1
?      ?       ?       file2
...

The fields are separated by tabs (\t). The fields are in order: linecount, wordcount, charactercount, filename.

"""
import sys


def filecount(filename):

    line_count = 0
    word_count = 0
    char_count = 0
    with open(filename) as f:
        for line in f:
            # line = line.strip("\n")

            words = line.split()
            line_count += 1
            word_count += len(words)
            char_count += len(line)
        return line_count, word_count, char_count


for arg in sys.argv[1:]:
    count = filecount(arg)
    print(f"{count[0]}\t{count[1]}\t{count[2]}\t{arg}")
