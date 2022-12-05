#!/usr/bin/env python3
def no_c(my_string):
    new_string = my_string[:]
    j = 0
    for c in range(len(my_string)):
        if my_string[c] == 'c' or my_string[c] == 'C':
            new_string = new_string[:(c - j)] + my_string[(c + 1):]
            j += 1
    return (new_string)
