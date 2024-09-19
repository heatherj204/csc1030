#!/usr/bin/env python3

def histogram(numList, replaceChar):
    for num in numList:
        num = int(num)
        line = replaceChar * num
        print(line)
histogram([6, 2, 15 , 3, 20 , 5], '=' )