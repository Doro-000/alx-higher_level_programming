#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as f:
        content = f.readlines()
        for i in range(len(content)):
            if search_string in content[i]:
                content.insert(i + 1, new_string)
        f.seek(0)
        f.truncate(0)
        f.writelines(content)
