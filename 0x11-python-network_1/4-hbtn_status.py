#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status using requests"""
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get(argv[1]).text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
