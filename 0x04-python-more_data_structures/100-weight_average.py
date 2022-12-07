#!/usr/bin/python3
"""
Returns the weighted average of all integers tuple (<score>, <weight>)
Returns 0 if the list is empty
Test file is 100-main.py
"""


def weight_average(my_list=[]):
    if not my_list:
        return (0)

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
