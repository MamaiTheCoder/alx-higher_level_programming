#!/usr/bin/python3

def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added
    """
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)
