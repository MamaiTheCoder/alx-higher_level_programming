#!/usr/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response.
# Check if a URL was provided as an argument

curl -Ls "$1"
