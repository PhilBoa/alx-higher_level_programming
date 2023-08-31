#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response (for status code 200)
[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" == "200" ] && curl -s "$1"
