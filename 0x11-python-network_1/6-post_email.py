#!/usr/bin/python3
"""
Takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter, and
finally displays the body of the response.
Command to run:
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
