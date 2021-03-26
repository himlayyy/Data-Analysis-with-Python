#!/usr/bin/env python3
"""
Let d be a dictionary that has English words as keys and a list of Finnish words as
values. So, the dictionary can be used to find out the Finnish equivalents of an
English word in the following way:

d["move"]
["liikuttaa"]
d["hide"]
["piilottaa", "salata"]
Make a function reverse_dictionary that creates a Finnish to English dictionary
based on a English to Finnish dictionary given as a parameter. The values of the
created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
"""
from collections import defaultdict

def reverse_dictionary(d):
    finn_eng_dict = defaultdict(list)
    for k,v in d.items():
        for i in v:
            finn_eng_dict[i].append(k)
    return dict(finn_eng_dict)


d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
print(reverse_dictionary(d))


