#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
echo $(curl -sv -o /dev/null "$1" 2>&1 | grep Allow | cut -d' ' -f3- )
