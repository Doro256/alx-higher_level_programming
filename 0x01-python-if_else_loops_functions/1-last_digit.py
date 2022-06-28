#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str = num_str[-1]
last_digit = int(last_digit_str)
str = "Last digit of " + number + " is " + last_digit

if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print(str + " and is greater than 5")
if last_digit == 0:
    print(str + " and is 0")
if last_digit < 6 and not 0:
    print(str + " and is less than 6 and not 0")
