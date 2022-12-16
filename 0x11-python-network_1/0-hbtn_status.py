#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        utf8_body = page.decode("utf-8")
        print("\t- utf8 content: {}".format(page))
