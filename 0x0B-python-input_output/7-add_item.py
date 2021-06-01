#!/usr/bin/python3
import sys
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)

def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

try:
    my_list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
except FileNotFoundError:
    with open("add_item.json", "w") as f:
        json.dump([], f)
