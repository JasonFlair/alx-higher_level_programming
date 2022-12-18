#!/usr/bin/python3
"""
a Python script that fetches a URL
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(sys.argv[1])
    id_header_value = response.headers['X-Request-Id']
    """
    retrieves the value of the X-Request-Id key and stores
    to a variable
    """
    print(id_header_value)
