#!/usr/bin/python3
""" contains find_peak """


def find_peak(list_of_integers):
        """finds a peak in a list of unsorted integers"""
        if (not list_of_integers):
                return None
        if (len(list_of_integers) == 1):
                return list_of_integers[0]
        half = len(list_of_integers) // 2
        list_1 = list_of_integers[0: half]
        avg_1 = sum(list_1) / len(list_1)
        list_2 = list_of_integers[half:]
        avg_2 = sum(list_2) / len(list_2)
        if (avg_1 > avg_2):
                return find_peak(list_1)
        elif (avg_1 < avg_2):
                return find_peak(list_2)
        else:
                return max(find_peak(list_1), find_peak(list_2))
