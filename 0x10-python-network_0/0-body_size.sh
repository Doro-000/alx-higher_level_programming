#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body
echo $(curl -Is "$1" 2>&1 | grep Content-Length | cut -d' ' -f2)
