#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body
echo $(curl -fLs "$1")
