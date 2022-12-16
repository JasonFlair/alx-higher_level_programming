<<<<<<< HEAD
#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    status_page = response.read()
    print("Body Response:")
    print(f"    - type: {type(status_page)}")
    print(f"    - content: {status_page}")
    utf8_body = status_page.decode("utf-8")
    print(f"    - utf 8 content: {utf8_body}")
=======
#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    status_page = response.read()
>>>>>>> 21ab7e9b605ade3c82e2ad77dfa6ab23a7b18c04
