#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    print("{:n} {}".format(argc-1, "argument." if argc == 1 else "arguments:"))
    for arg in range(1, argc):
        print("{:n}: {}".format(arg, sys.argv[arg]))
