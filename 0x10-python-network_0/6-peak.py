#!/usr/bin/python3
""" contains find_peak """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if (not list_of_integers):
        return None
    if (len(list_of_integers) == 1):
        return list_of_integers[0]
    peak_1 = find_peak(list_of_integers[0: len(list_of_integers) // 2])
    peak_2 = find_peak(list_of_integers[len(list_of_integers) // 2:])
    return max(peak_1, peak_2)
