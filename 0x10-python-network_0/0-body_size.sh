#!/usr/bin/env bash
# takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

size=$(curl -Is "$1" 2>&1 | grep Content-Length | cut -d' ' -f2)
echo "$size"
