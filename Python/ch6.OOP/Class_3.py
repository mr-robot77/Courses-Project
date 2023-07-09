# Define variable for Object
>>> class Person:
...     pass
...
>>> p1 = Person()
>>> p2 = Person()
>>> p1.name = 'mohamadreza'
>>> p1.age = 18
>>> p1.name
mohamadreza
>>> p1.age
18
>>> p2.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute 'name'
>>> p2.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute 'age'