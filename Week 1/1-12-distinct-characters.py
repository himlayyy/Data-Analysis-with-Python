#!/usr/bin/env python3
""""
Write function distinct_characters that gets a list of strings as a
parameter. It should return a dictionary whose keys are the strings
the input list and the corresponding values are the numbers of distinct
characters in the key.

Use the set container to temporarily store the distinct characters in a
string. Example of usage:
distinct_characters(["check", "look", "try", "pop"])
should return { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}."""


def distinct_characters(L):
    numbers = list(map(len, (map(set, L))))
    return dict(zip(L, numbers))


print(distinct_characters(["check", "look", "try", "pop"]))
