#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    length = len(my_list)

    copy = my_list[:]
    
    if idx >=  0 and idx < (len(my_list) - 1):
        copy[idx] = element
    return (copy) 
