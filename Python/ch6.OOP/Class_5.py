# using constructor function for class properties
>>> class Person:
...     def __init__(self, name, age=18):
...         self.name = name
...         self.age = age
...
>>> p1 = Person("Ali", 12)
>>> p2 = Person("Amir")
>>> p1.name
'Ali'
>>> p1.age
12
>>> p2.name
'Amir'
>>> p2.age
18