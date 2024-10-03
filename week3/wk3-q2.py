#!/usr/bin/env python3

def reverseInt(n, num=0):
    if n == 0:
        return num
    lastDig = n % 10
    num = (num * 10) + lastDig
    n = (n // 10)
    return reverseInt(n, num)



print(reverseInt(123))