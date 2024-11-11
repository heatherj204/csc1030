#!/usr/bin/env python3

class MySortedList:
    def __init__(self) -> None:
        self.sortedList = []

    def getIndex(self, key):
        low = 0; high = len(self.sortedList) - 1
        while low <= high:
            mid = (low + high) // 2

            if key == self.sortedList[mid][0]:
                return mid
            elif key < self.sortedList[mid][0]:
                high = mid - 1
            elif key < self.sortedList[mid][0]:
                low = mid + 1
        return low

    def inset(self, key, value):
        index = self.getIndex(key)
        if index < len(self.sortedList) and self.sortedList[index][0] == key:
            self.sortedList[index] = (key, value)
        else:
            self.sortedList.insert(index, (key, value))

    def display(self):
        return '\n'.join(str(s) for s in self.sortedList)

sortedMap = MySortedList()
sortedMap.inset('2024-11-04T15:10:42Z', 'Transaction D')
sortedMap.inset('2024-11-02T17:10:42Z', 'Transaction C')
#sortedMap.inset('2024-11-05T16:10:42Z', 'Transaction E')

print(sortedMap.display())