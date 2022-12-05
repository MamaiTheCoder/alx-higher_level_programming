#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy_of_list = my_list[:]
        return copy_of_list
    elif idx > len(my_list):
        copy_of_list = my_list[:]
        return copy_of_list
    else:
        copy_of_list = my_list[:]
        copy_of_list[idx] = element
        return copy_of_list
