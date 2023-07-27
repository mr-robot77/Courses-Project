# getattr() function

>>> class A:
...     def __init__(self, age, name):
...         self.age = age
...         self.name = name
... 
>>> 
>>> a = A(12, 'amir')
>>> print(getattr(a, 'age'))
12
>>> s = input()
name
>>> print(getattr(a, s))
amir

# optional argument >> default

>>> a = 0
>>> print(getattr(a, 'age', 12))
12

# setattr() function

>>> class A:
...     pass
... 
>>> a = A()
>>> setattr(a, 'name', 'amir')
>>> setattr(a, 'age', 12)
>>> print(a.name + " , " + str(a.age))
amir , 12

# define function into dynamic

class A:
    def __init__(self):
        self.attrs = {'name': 'amir', 'age': 12, 'grade': 'A'}

    def __getattr__(self, attr):

        if attr in self.attrs:
            return self.attrs[attr]

        def f():
            return getattr(self, attr[4:])

        return f

a = A()

print(a.get_name())
print(a.get_age())
print(a.get_grade())

amir
12
A