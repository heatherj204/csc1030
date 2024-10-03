def findLen(str, strlen=0):
    if str == "":
        return strlen
    strlen += 1
    str = str[:-1]
    return findLen(str, strlen)

print(findLen("Hello"))