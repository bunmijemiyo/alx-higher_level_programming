#!/usr/bin/python3
"""
- takes in Github credentials as arguments
    - 1st arg:  username
    - 2nd arg:  password
- uses Github API to display user Id
"""

if __name__ == '__main__':
    import sys
    from requests.auth import HTTPBasicAuth
    import requests

    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    res = requests.get('https://api.github.com/user', auth=basic)
    res = res.json()
    print(res.get('id'))
