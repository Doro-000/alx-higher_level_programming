#!/usr/bin/python3


def print_matrix_integer(my_list=[[]]):
    if not my_list:
        return None
    if not my_list[0] and len(my_list) == 1:
        print("")
    for row in my_list:
        for element in range(len(row)):
            if element < len(row)-1:
                print("{:d}".format(row[element]), end=" ")
            else:
                print("{:d}".format(row[element]))
