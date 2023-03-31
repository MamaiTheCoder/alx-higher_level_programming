#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code.
Command to run - ./7-error_code.py http://0.0.0.0:5000
                 ./7-error_code.py http://0.0.0.0:5000/status_401
                 ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
                 ./7-error_code.py http://0.0.0.0:5000/status_500
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
