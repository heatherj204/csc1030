#!/usr/bin/env python3

def multiply(num1, num2):
    if (num1 or num2 < 0):
        if num1 == -1:
            return -1
        elif num2 == 0:
            return 0

        return num1 + (multiply(num1, num2 + 1))
    else:
        if num1 == -1:
            return -1
        elif num2 == 0:
            return 0
        return num1 + (multiply(num1, num2 - 1))

print(multiply(10, 12))