#!/usr/bin/python3
"""
Returns the number of keys in a dictionary.
Test file is 5-main.py
"""


def number_keys(a_dictionary):
    number_of_keys = 0
    show_keys = a_dictionary.keys()

    for i in show_keys:
        number_of_keys += 1

    return (number_of_keys)
