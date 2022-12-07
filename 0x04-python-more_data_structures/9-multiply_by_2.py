#!/usr/bin/python3
"""
Returns a new dictionary with all values multiplied by 2
Assume that all values are only integers
Returns a new dictionary
Test file is 9-main.py
"""


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()

    show_keys = list(new_dictionary.keys())

    for i in show_keys:
        new_dictionary[i] *= 2
    return (new_dictionary)
