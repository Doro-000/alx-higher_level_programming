#!/usr/bin/python3
"""sends a POST request to argv[1] with email attached, and displays the result"""
from urllib import request, parse
from sys import argv

data = {"email":argv[2]}
data = parse.urlencode(data).encode('ascii')
req = request.Request(argv[1], data)
with request.urlopen(req) as response:
	print(response.read().decode('utf-8'))
