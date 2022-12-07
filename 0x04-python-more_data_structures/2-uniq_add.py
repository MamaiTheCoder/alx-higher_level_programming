#!/usr/bin/python3
"""
Adds all unique integers in a list (only once for each integer).
Test file is 2-main.py
"""


def uniq_add(my_list=[]):
    new_list = set(my_list)
    result = 0

    for i in new_list:
        result += i
    return (result)
