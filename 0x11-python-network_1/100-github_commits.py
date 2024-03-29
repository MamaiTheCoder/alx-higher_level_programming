#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.
The first argument will be the repository name.
The second argument will be the owner name.
List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
