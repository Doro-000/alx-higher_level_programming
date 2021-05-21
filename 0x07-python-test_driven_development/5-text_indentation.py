#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    result = []
    for char in text:
        result.append(char)
        if char in ['.', '?', ':']:
            result.append("\n\n")
    print("".join(result), end="")
    
