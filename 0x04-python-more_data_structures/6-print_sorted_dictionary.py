#!/usr/bin/python3
"""
Prints a dictionary by ordered keys.
Test file is 6-main.py
"""


def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())

    list_ord.sort()

    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
