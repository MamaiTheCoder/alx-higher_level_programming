#!/usr/bin/python3
"""LockedClass module.
Containts a clas that avoids
dynamically created attributes
"""


class LockedClass:
    """LockedClass class containing  only __slots__."""
    __slots__ = ['first_name']

    def __init__(self):
        """init method"""
        pass
