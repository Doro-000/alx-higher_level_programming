#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{:n} is zero\n".format(number))
elif number > 0:
    print("{:n} is positive\n".format(number))
else:
    print("{:n} is negative\n".format(number))
