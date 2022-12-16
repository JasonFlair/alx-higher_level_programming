#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as response:
        status_page = response.read()
        print("Body Response:")
        print(f"\t- type: {type(status_page)}")
        print(f"\t- content: {status_page}")
        utf8_body = status_page.decode("utf-8")
        print(f"\t- utf8 content: {utf8_body}")
