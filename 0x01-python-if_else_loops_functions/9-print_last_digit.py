#!/usr/bin/python3


def print_last_digit(number):
    print("{:n}".format(number % 10), end="")
    return number % 10
