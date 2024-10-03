#!/usr/bin/env python3

def reverseLst(lst, revLst=None):
    if revLst == None:
        revLst = []

    if lst == []:
        return revLst
    lastItem = lst[-1]
    revLst.append(lastItem)
    lst.pop()
    return reverseLst(lst, revLst)

print(reverseLst([1, 2, 3, 4]))