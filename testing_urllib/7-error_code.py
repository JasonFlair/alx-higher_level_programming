#!/usr/bin/python3
"""
a Python script that fetches a URL
"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        url = sys.argv[1]
        response = requests.get(url)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e}")
