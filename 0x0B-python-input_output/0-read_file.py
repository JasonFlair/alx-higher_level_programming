#!/usr/bin/python3
"""read a file and print to stdout."""

def read_file(filename=""):
    """
    function to read a file and print to stdout
    :param filename: filename
    :return: a print of the read file to stdout
    """
    with open(filename, "r", encoding="utf-8") as FILE:
        read_FILE = FILE.read()
        print(read_FILE, end="")
