#!/usr/bin/python3
"""
Takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
Command to run:
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
