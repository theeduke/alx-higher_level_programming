#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number %  10
if rem > 5:
    print("Last digit of {} is {} and is greater than 5 \n".format(number, rem))

if rem == 5:
    print("Last digit of {} is {} and is greater than 5 \n".format(number, rem))

if rem < 6 and rem != 0: 
    print("Last digit of {} is {} and is greater than 5 \n".format(number, rem))
