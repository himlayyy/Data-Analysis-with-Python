#!usr/bin/env python3
"""
The file src/listing.txt contains a list of files with one line per file. Each line contains seven fields:
access rights, number of references, owner’s name, name of owning group, file size, date, filename.
These fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.

Write function file_listing that loads the file src/listing.txt. It should return a list of tuples (size, month, day,
hour, minute, filename). Use regular expressions to do this (either match, search, findall, or finditer method).

An example: for line

-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf").

"""
import re


def file_listing(filename):
    pattern = re.compile(r'\s+(\d+)\s*(Oct|Nov|Dec)\s*(\d+)\s(\d+):(\d+)\s(.+)\s')
    meta = []
    with open(filename) as f:
        for line in f:
            details = pattern.search(line)
            meta.append((int(details.group(1)), details.group(2), int(details.group(3)), int(details.group(4)),details.group(5), details.group(6)))
    return meta

print(file_listing(r"listing.txt"))


