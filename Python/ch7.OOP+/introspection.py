# dir() function

>>> class Person:
...     def get_age(self):
...             pass
...     name = 'Saeid'
... 
>>> person = Person()
>>> dir(person)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_age', 'name']

>>> number = 100
>>> def func():
...     number_2 = 200
...     print(dir())
... 
>>> func()
['number_2']

# type() function

>>> a = 100
>>> type(a)
<class 'int'>
>>> a = [1, 2, 3]
>>> type(a)
<class 'list'>
>>> def func():
...     pass
... 
>>> type(func)
<class 'function'>
>>> type(type)
<class 'type'>

>>> def set_name(self, name):
...     self.name = name
... 
>>> Kid = type('MyNewType', (object,), {'age': 4, 'height': 130, 'name': 'default', 'set_name': set_name})
>>> kid = Kid()
>>> kid.age
4
>>> kid.height
130
>>> kid.name
'default'
>>> kid.set_name('amir')
>>> kid.name
'amir'
>>> type(Kid)
<class 'type'>
>>> type(kid)
<class '__main__.MyNewType'>

>>> class Person():
...     name = ''
...     age = 8
... 
>>> Kid = type('Kid', (Person,), {'height': 130})
>>> kid = Kid()
>>> kid.name
''
>>> kid.age
8
>>> dir(kid)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'height', 'name']

# isinstance() function

>>> class Animal:
...     def __init__(self, name, type):
...         self.name = name
...         self.type = type
...  
>>> class Fox(Animal):
...     def __init__(self, name):
...         self.name = name
...         self.type = 'Fox'
... 
>>> class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
... 
>>> fox = Fox('Alex')
>>> isinstance(fox, Fox)
True
>>> isinstance(fox, Animal)
True
>>> isinstance(fox, Person)
False
>>> isinstance(fox, (Animal, Person))
True
>>> isinstance(fox, (list, Person))
False
>>> isinstance(2, int)
True
>>> isinstance(2, str)
False
>>> isinstance(2, (str, list, int, float))
True

# issubclass() function

>>> class Animal:
...     def __init__(self, name, type):
...         self.name = name
...         self.type = type
... 
>>> class Bird(Animal):
...     def __init__(self, name):
...         self.name = name
...         self.type = 'Bird'
... 
>>> class Owl(Bird):
...     def __init__(self, name):
...         self.name = name
...         self.type = 'Bird'
...         self.bird_type = 'Owl'
... 
>>> class Person:
...     def __init__(self, name. age):
...         self.name = name
...         self.age = age
...
>>> issubclass(Bird, Animal)
True
>>> issubclass(Owl, Animal)
True
>>> issubclass(Animal, Owl)
False
>>> issubclass(Person, Animal)
False
>>> issubclass(Animal, object)
True
‌>>> issubclass(Owl, (Animal, Person))
True
>>> issubclass(Bird, (Person, list, Owl))
False

