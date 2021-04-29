#!/usr/bin/python3
from test import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)

if __name__ == "__main__":
    from dis import dis
    print(dis(magic_calculation))
