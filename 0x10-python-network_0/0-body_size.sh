#!/usr/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response.
# curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2

# Check that a URL was provided as an argument
if [ -z "$1" ]; then
  echo "Error: no URL provided"
  exit 1
fi

# Send a GET request to the URL and capture the response in a variable
response=$(curl -sI "$1")

# Extract the content length from the response headers using awk
content_length=$(echo "$response" | awk '/Content-Length/ {print $2}')

# Check if the content length was found
if [ -z "$content_length" ]; then
  echo "Error: could not determine content length"
  exit 1
fi

# Display the content length in bytes
echo "$content_length"


