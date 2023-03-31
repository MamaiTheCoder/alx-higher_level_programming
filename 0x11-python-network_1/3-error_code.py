#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
command to run - ./3-error_code.py http://0.0.0.0:5000
                 ./3-error_code.py http://0.0.0.0:5000/status_401
                 ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
                 ./3-error_code.py http://0.0.0.0:5000/status_500
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
