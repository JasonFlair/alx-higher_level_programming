#!/usr/bin/python3
"""
a Python script that fetches a URL and handles exceptions
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    from urllib.error import URLError, HTTPError

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(f"{page}")
    except HTTPError as e:
        print(f'Error code: {e.code}')
    except URLError as e:
        print(f"Error code: {e.reason}")
