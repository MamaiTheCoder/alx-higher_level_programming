#!/usr/bin/python3
def print_last_digit(number):
	if number < 0:
		ABSNum = number * -1
	else:
		ABSNum = number
	lastDig = ABSNum % 10
	print("{:d}".format(lastDig), end='')
	return (lastDig)
