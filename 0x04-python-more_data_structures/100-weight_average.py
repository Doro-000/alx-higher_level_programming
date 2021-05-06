#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for int_tup in my_list:
        numerator += int_tup[0] * int_tup[1]
        denominator += int_tup[1]
    return numerator / denominator
