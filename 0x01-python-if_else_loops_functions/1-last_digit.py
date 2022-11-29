#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	number1 = number * -1
else:
	number1 = number
lstDigit = number1 % 10

if lstDigit > 5:
	print(f"Last digit of {number} is {lstDigit} and is greater than 5")
elif lstDigit == 0:
	print(f"Last digit of {number} is {lstDigit} and is 0")
else:
	print(f"Last digit of {number} is {lstDigit} and is less than 6 and not 0")   
