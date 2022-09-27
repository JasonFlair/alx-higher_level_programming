#!/usr/bin/python3
"""write a file."""

def write_file(filename="", text=""):
    """
    function to count characters
    :param filename: filename
    :param text: text to count
    :return: a print of the read file to stdout
    """
    with open(filename, "w", encoding="UTF-8") as FILE:
        written_FILE = FILE.write(text)
        return written_FILE
