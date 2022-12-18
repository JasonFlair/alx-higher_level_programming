#!/usr/bin/python3
"""
a Python script that fetches a URL
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    authentication = {username, password}

    response = requests.get(url, auth=authentication)
    print(response.text)
    print(response.headers)
    print(response.headers["id"])
