#!/usr/bin/python3
"""
Replaces all occurrences of an element by another in a new list
Test file is 1-main.py
"""


def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
