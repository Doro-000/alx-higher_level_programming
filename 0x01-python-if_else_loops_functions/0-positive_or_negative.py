#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{:n} is zero".format(number))
elif number > 0:
    print("{:n} is positive".format(number))
else:
    print("{:n} is negative".format(number))
