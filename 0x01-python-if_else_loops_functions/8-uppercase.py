#!/usr/bin/python3
def uppercase(str):
    for ch in range(len(str)):
        chnum = ord(str[ch])
        if chnum >= 97 and chnum <= 122:
            chnum -= 32
        print("{:c}".format(chnum), end='')
    print()
