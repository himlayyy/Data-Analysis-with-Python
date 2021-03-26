#!usr/bin/env python 3
"""Write a function positive_list that gets a list of numbers as a parameter, and returns
a list with the negative numbers and zero filtered out using the filter function.

The function call positive_list([2,-2,0,1,-7]) should return the list [2,1]. Test your
function in the main function.

"""
# def is_odd(x):
#     """Returns True if x is odd and False if x is even"""
#     return x % 2 == 1         # The % operator returns the remainder of integer division
# L=[1, 4, 5, 9, 10]
# print(list(filter(is_odd, L)))
# !/usr/bin/env python3

def positive_list(nums):
    return list(filter(lambda x: x > 0, nums))


def main():
    print(positive_list([2, -2, 0, 1, -7]))


if __name__ == "__main__":
    main()
