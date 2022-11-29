#!/usr/bin/python3
for firstDig in range(0, 10):
	for secondDig in range(0, 10):
		if firstDig >= secondDig:
			continue
		if firstDig == 8 and secondDig == 9:
			print("{:d}{:d}".format(firstDig, secondDig))
		else:
			print("{:d}{:d}, ".format(firstDig, secondDig), end='')
