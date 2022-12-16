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
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        utf8_body = page.decode("utf-8")
        print(f"\t- utf8 content: {page}")
