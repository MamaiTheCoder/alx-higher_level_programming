#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
Command to run - ./4-hbtn_status.py | cat -e
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
