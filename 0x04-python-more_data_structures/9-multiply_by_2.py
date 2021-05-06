#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_keys = list(map(lambda a: a*2, a_dictionary.values()))
    return dict([(key, val) for key, val in zip(a_dictionary.keys(), new_keys)])
