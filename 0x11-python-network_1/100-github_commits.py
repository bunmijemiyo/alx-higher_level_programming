#!/usr/bin/python3
"""
takes in username and repo name as argument respectively
list 10 commits (recent to oldest) of the github repo
"""

if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    res = requests.get(url)
    res = res.json()
    try:
        for i in range(0, 10):
            print(f"{res[i].get('sha')}: {res[i]['commit']['author']['name']}")
    except IndexError:
        pass
