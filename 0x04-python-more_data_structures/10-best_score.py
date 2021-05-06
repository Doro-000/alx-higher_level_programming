#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    g = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[g]:
            g = key
    return g
