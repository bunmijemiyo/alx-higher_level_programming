#!/usr/bin/python3
"""
sends a request and displays the body of the error
display error code if HTTPError is encountered
"""

if __name__ == '__main__':
    from urllib.error import HTTPError
    from urllib import request
    import sys

    try:
        with request.urlopen(sys.argv[1]) as res:
            res = res.read().decode('UTF-8')
            print(res)
    except HTTPError as exception:
        print('Error code:', exception.code)
