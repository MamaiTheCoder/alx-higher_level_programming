#!/usr/bin/python3
"""
Returns a key with the biggest integer value.
Assume that all values are only integers.
Assume all students have a different score.
If no score found, return None.
Test file is 10-main.py
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
