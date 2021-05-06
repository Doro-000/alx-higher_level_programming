#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    greatest = list(a_dictionary.values())[0]
    compare = lambda a: a_dictionary[a] > greatest
    return list(filter(compare, a_dictionary.keys())[-1]
