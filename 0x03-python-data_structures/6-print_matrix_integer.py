#!/usr/bin/python3


def print_matrix_integer(my_list=[[]]):
    if (not my_list) or (not mylist[0]):
        print("")
        return None
    for row in my_list:
        for element in range(len(row)):
            if element < len(row)-1:
                print("{:d}".format(row[element]), end=" ")
            else:
                print("{:d}".format(row[element]))
