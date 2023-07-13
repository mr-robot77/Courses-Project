
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name):
        self.name = name

# this two code is the same

class Person:
    def __init__(self, name):
        self.name = name
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
class Person(object):
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Worker(Person):
    pass

class Teacher(Person):
    pass

class Engineer(Person):
    pass

class Person:
    def __init__(self):
        print('Initialize from class Person')

class Engineer(Person):
    def __init__(self):
        print('Initialize from class Engineer')
        Person.__init__(self)

eng = Engineer()

Initialize from class Engineer
Initialize from class Person

# using super() for inheritence from father class functions call

class Person:
    def __init__(self):
        print('Initialize from class Person')

class Engineer(Person):
    def __init__(self):
        print('Initialize from class Engineer')
        super().__init__()

eng = Engineer()

Initialize from class Engineer
Initialize from class Person

class Person:
    def __init__(self):
        print('Initialize from class Person')

    def output(self):
        print('Output from class Person')

class Engineer(Person):
    def __init__(self):
        print('Initialize from class Engineer')

    def output(self):
        print('Output from class Engineer')
        super().output()

sepehr= Engineer()
sepehr.output()

Initialize from class Engineer
Output from class Engineer
Output from class Person

# important inheritence functions

>>> isinstance(5, int)
True
>>> isinstance(5, str)
False
>>> isinstance('Hello', int)
False
>>> isinstance("Hello", (float, str, int, list, dict, tuple))
True
>>> isinstance(5 , (float, str, list, dict, tuple))
False

class ‌Worker:
  pass

class Teacher:
  pass

y = Worker()
x = isinstance(y, Worker)
print(x)
x = isinstance(y, Teacher)
print(x)
x = isinstance(y, (Worker, Teacher))
print(x)

True
False
True

class Person:
  pass

class Worker(Person):
  pass

class Animal:
  pass

x = issubclass(Worker, Person)
print(x)
x = issubclass(Animal, Person)
print(x)

True
False