#!/usr/bin/env python3

def filter_star(dict, rating):
    chocoDict = {}
    for k, v in dict.items():
        if len(v) == rating:
            chocoDict[k] = v
    if len(chocoDict) > 0:
        return chocoDict
    else:
        return "No result found!"

res1 = filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 4)

print(res1)

res2 = filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 2)

print(res2)
