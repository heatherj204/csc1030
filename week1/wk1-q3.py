#!/usr/bin/env python3

class Memories():
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)
    def remember(self, key):
        return(getattr(self, key, False))

person1 = Memories(name='Tom', age=32, salary=50000)
print(person1.remember('salary'))
print(person1.remember('email'))