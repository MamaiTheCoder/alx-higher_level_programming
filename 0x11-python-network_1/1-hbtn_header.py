#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response.
command to run - ./1-hbtn_header.py https://alx-intranet.hbtn.io
"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
