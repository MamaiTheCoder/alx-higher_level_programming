#!/usr/bin/python3
"""
Contains the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from.
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
