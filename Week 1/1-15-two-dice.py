#!usr/bin/env python 3
"""Redo the earlier exercise which printed all the pairs of two dice results that sum to 5. But this time use a list
comprehension. Print one pair per line."""

# for dice1 in range(1,7):
#     for dice2 in range(1,7):
#         if dice1 + dice2 == 5:
#             print(dice1, dice2)
# print("\n".join(f"({dice1},{dice2})" for dice2 in range(1,7) for dice1 in range(1,7) if dice1 + dice2 == 5))
sum_five = [(dice1,dice2) for dice2 in range(1,7) for dice1 in range(1,7) if dice1 + dice2 == 5]
for item in sum_five:
    print(item,end="\n")

print(("\n".join(f"({x},{y})" for y in range(1, 7) for x in range(1, 7) if x + y == 5)))