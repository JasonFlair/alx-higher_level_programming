#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        utf8_body = page.decode("utf-8")
        print("\t- utf8 content: {}".format(page))
