#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the response, handles exceptions"""
from urllib import request, error
from sys import argv

try:
	response = request.urlopen(argv[1])
	print(response.read().decode('utf-8'))
except error.HTTPError as http_err:
	print("Erro code: {}".format(http_err.code))
