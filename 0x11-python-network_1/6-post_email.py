#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

import requests

if __name__ == "__main__":
    url = sys.argv[1]
    header = {"email": f"{sys.argv[2]}"}
    """
    named the variable header instead of headers 
    because the only header being passed is email
    """
    response = requests.get(url, headers=header)
    print(f"Your email is: {response.headers['email']}")

