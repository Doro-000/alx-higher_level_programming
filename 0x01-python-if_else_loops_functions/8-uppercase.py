#!/usr/bin/python3


def uppercase(str):
    for char in str:
        char = (ord(char) - 32) if 97 <= ord(char) <= 122 else ord(char)
        print("{:c}".format(char), end="")
    print("")
