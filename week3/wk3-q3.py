#!/usr/bin/env python3

def reverseString(line, revLine=""):
    if line == "":
        return revLine
    lastChar = line[-1]
    revLine += lastChar
    line = line[:-1]
    return reverseString(line, revLine)

print(reverseString("hello"))
