#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
Command to run - ./8-json_api.py
                 ./8-json_api.py a
                 ./8-json_api.py 2
                 ./8-json_api.py b
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
