#!/bin/bash
# This script makes a request to the server and causes it to respond with the message "You got me!"
curl -sLX PUT "$1/catch_me"
