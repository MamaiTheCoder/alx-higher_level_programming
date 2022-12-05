#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    length = len(my_list)

	if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    new_list = [x  for x in my_list]
    new_list[idx] = element
    return (new_list)
