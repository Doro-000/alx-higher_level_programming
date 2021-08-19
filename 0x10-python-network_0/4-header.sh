#!/bin/bash
# sends a GET request to the URL
echo $(curl -sH "X-HolbertonSchool-User-Id: 98" "$1")
