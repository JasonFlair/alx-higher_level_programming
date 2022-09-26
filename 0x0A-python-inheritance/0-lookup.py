#!/usr/bin/python3

def lookup(obj):
    for attribute in dir(obj):
        print(attribute, getattr(obj, attribute))
