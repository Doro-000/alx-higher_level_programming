#!/usr/bin/python3
"""sends a request to argv[1] and displays the value of X-Request-Id in the header"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
	print(response.getheader("X-Request-Id"))
