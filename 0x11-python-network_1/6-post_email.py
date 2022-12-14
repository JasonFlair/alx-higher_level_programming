#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email_data = {"email": f"{sys.argv[2]}"}
    response = requests.post(url, data=email_data)
    print(response.text)
