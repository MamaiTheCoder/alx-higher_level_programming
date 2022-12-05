#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    length = len(my_list)

    copy_of_list = my_list[:]
    if idx >= 0 and idx < length:
        copy_of_list[idx] = element
    return (copy_of_list)
