#!usr/bin evn python 3
"""Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order.
Create a function merge that gets these lists as parameters and returns a new sorted list L that
has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the
fact that both lists are already sorted. You can’t use the sorted function or the sort method in
 the merge method. You can however use these sorted in the main function for creating inputs to
 the merge function. Test with a couple of examples in the main function that your solution
 works correctly"""
import random


def merge(list1, list2):
    sorted_list = list1 + list2
    final_list = []
    print(sorted_list)
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    print(sorted_list)


l1 = sorted(random.sample(range(100), 10))
l2 = sorted(random.sample(range(100), 10))
print(l1,"\n",l2)
merge(l1, l2)
