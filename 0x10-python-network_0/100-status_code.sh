#!/bin/bash
# displays only the status code of an http request
echo $(curl -s -w "%{http_code}" -o /dev/null "$1")
