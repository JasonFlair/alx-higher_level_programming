#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {'email': ''.format(sys.argv[2])}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')  # data should be bytes
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        headers = response.info()
        print(f"Your email is {headers['email']}")
