#!/usr/bin/python3
num = 122
while (num >= 97):
    if num % 2 == 0:
        print("{:c}".format(num), end='')
    else:
        print("{:c}".format(num - 32), end='')
    num = num - 1
