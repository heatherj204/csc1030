#!/usr/bin/env python3

def q1_sum(text):
    total = 0
    i = 0
    while i < len(text):
        j = 0
        newline= text[i]
        while j < len(newline):
            number = int(newline[j])
            if (number % 2 == 0):
                total += number
            j += 1
        i += 1
    return total
print(q1_sum([
    [1, 0, 2],
    [5, 5, 7],
    [9, 4, 3]]))