#!/usr/bin/env python3

def move_vow(text):
    vowels = 'aeiouAEIOU'
    vowonly = ''
    constonly = ''
    for letter in text:
        if letter in vowels:
            vowonly += letter
        else:
            constonly += letter
    vowfirst = vowonly + constonly
    return vowfirst

print(move_vow('This is DCU!'))