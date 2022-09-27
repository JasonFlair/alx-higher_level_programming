#!/usr/bin/python3
"""read a file and print to stdout."""

def read_file(filename=""):
    """function to read a file and print to stdout"""
    with open(filename, "r", encoding="UTF-8") as FILE:
        read_FILE = FILE.read()
        print(read_FILE)
