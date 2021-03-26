#!/usr/bin/env python3
"""Create a function named detect_ranges that gets a list of integers as a parameter. The function
should then sort this list, and transform the list into another list where pairs are used for all
the detected intervals. So 3,4,5,6 is replaced by the pair (3,7).
Numbers that are not part of any interval result just single numbers.
The resulting list consists of these numbers and pairs, separated by commas. An example of how
this function works:
print(detect_ranges([2,5,4,8,12,6,7,10,13]))
[2,(4,9),10,(12,14)]
Note that the second element of the pair does not belong to the range. This is consistent with
the way Python’s range function works. You may assume that no element in the input list appears multiple times."""


def detect_ranges(l):
    sorted_l = sorted(l)
    print(sorted_l)
    temp_list = []
    for item in sorted_l:
        if item + 1 not in sorted_l:
            temp_list.append(item)
        else:
            start = item
            end = item
            while end + 1 in sorted_l:
                end = end + 1
                sorted_l.remove(end)
            t = (start, end+1)
            temp_list.append(t)
    return temp_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(result)

if __name__ == "__main__":
    main()
