#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        arg = "arguments."
    elif argc == 2:
        arg = "argument:"
    else:
        arg = "arguments:"
    print("{:n} {}".format(argc-1, arg))
    for arg in range(1, argc):
        print("{:n}: {}".format(arg, sys.argv[arg]))
