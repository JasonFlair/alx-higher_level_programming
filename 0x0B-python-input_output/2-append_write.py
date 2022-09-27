#!/usr/bin/python3
"""write a file."""

def append_write(filename="", text=""):
    """
    function to count characters
    :param filename: filename
    :param text: text to append
    :return: a count of the appended text
    """
    with open(filename, "a", encoding="UTF-8") as FILE:
        appended_FILE = FILE.write(text)
        return appended_FILE
