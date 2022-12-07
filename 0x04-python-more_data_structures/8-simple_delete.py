#!/usr/bin/python3
"""
Deletes a key in a dictionary.
key argument will be always a string
If a key doesn’t exist, the dictionary won’t change
Test file is 8-main.py
"""


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
