#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.info()

        # Display the value of the variable from the header of the response
        print(headers['X-Request-Id'])
