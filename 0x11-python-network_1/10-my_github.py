#!/usr/bin/python3
"""
a Python script that fetches a URL
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    # Get the username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Set the basic authentication credentials
    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)
    response = response.json()
    print(response.get("id"))
