#!/usr/bin/python3
"""
Returns a list with all values multiplied by a number using maps.
Initial list should not be modified.
Test file is 11-main.py
"""


def multiply_list_map(my_list=[], number=0):
    return(list(map(lambda x: x * number, my_list)))
