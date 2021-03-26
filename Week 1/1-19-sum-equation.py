#!usr/bin/env python 3
"""Write a function sum_equation which takes a list of positive integers
as parameters and returns a string with an equation of the sum of the elements.

Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces
should be exactly as shown above. For an empty list the function should
return the string “0 = 0”
"""
import string

def sum_equation(nums):
    if not nums:
        return "0 = 0"
    else:
        equation = " + ".join(map(str, nums))
        full_eq = equation + " = " + str(sum(nums))
        return full_eq

print(sum_equation([1,5,7]))

