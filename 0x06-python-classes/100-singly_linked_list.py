#!/usr/bin/python3
"""Classes to implement a linked list"""


class Node():
    """Class to implement a Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        return self.__data
    @property
    def next_node(self):
        return self.__next_node
    
    @data.setter
    def data(self, value):
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if (type(value) == Node) or (value == None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Class to implement a singly linked list"""
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        new_node = Node(value, None)
        if (not self.__head):
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            largest = self.__head
            while (largest.next_node != None and largest.next_node.data < value):
                largest = largest.next_node
            new_node.next_node = largest.next_node
            largest.next_node = new_node
    def __str__(self):
        result = []
        string = ""
        largest = self.__head
        while (largest != None):
            result.append(str(largest.data))
            largest = largest.next_node
        return "\n".join(result)
