#!/usr/bin/python3
"""write a file."""

def write_file(filename="", text=""):
    """
    function to count characters
    :param filename: filename
    :param text: text to count
    :return: writes into specified file
    """
    with open(filename, "w", encoding="UTF-8") as FILE:
        written_FILE = FILE.write(text)
        return written_FILE
