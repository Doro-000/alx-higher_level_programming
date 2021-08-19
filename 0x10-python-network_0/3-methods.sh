#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
curl -X OPTIONS -si "$1" 2>&1| grep Allow | cut -d' ' -f2-
