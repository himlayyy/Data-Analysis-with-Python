#!/usr/bin/env python 3

"""
Use two nested for loops in the main function to iterate through all possible combinations the pair
of dice can give. There are 36 possible combinations. Print all those combinations as (ordered)
pairs that sum to 5. For example, your printout should include the pair (2,3).
Print one pair per line.
"""
for dice_1 in range(1, 7):
    for dice_2 in range(1, 7):
        if dice_1 + dice_2 == 5:
            print(f"({dice_1}, {dice_2})")
