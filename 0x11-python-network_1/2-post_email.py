#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed UR
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from urllib import request, parse
    import sys

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode('utf-8')

    url = sys.argv[1]

    resp = request.Request(url, data)
    with request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
