#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    g = list(a_dictionary.values())[0]
    return list(filter(lambda a: a_dictionary[a] > g, a_dictionary.keys()))[-1]
