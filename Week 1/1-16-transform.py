#!usr/bin/env python 3
"""Write a function transform that gets two strings as parameters and returns a list
of integers. The function should split the strings into words, and convert these words
to integers. This should give two lists of integers.
Then the function should return a list whose elements are multiplication of two
integers in the respective positions in the lists.
For example transform("1 5 3", "2 6 -1")
should return the list of integers [2, 30, -3].

You have to use split, map, and zip functions/methods.
You may assume that the two input strings are in correct format."""
import math
def transform(list1, list2):
    l1 = list(map(int, (list1.split())))
    l2 = list(map(int, (list2.split())))
    products = [math.prod(items) for items in zip(map(int,(list1.split())), map(int, (list2.split())))]
    return products
print(transform("1 5 3", "2 6 -1"))