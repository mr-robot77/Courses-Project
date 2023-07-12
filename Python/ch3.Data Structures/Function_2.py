>>> def f(a=0, b=1):
...     return a+b
... 
>>> f(2, 3)
5
>>> f(2)
3
>>> f()
1

>>> def f(a=0, b):
...     return a+b


>>> def f(a, L=[]):
...     L.append(a)
...     return L
... 
>>> f(1)
[1]
>>> f(2)
[1, 2]
>>> f(3)
[1, 2, 3]

>>> def f(a, L=None):
...     if L == None:
...             L = []
...     L.append(a)
...     return L
... 
>>> f(1)
[1]
>>> f(2)
[2]
>>> f(2,f(1))
[1, 2]

>>> def f(a, *args):
...     return args
... 
>>> f(2)
()
>>> f(2, 1)
(1,)
>>> f(1, 2, 3)
(2, 3)

>>> def f(*args, **kwargs):
...     print(args)
...     print(kwargs)
... 
>>> f(a=2)
()
{'a': 2}
>>> f(1, a=2)
(1,)
{'a': 2}
>>> f(1, a=2, 2)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument

>>> def printUsers(**users):
...     for name,age in users.items():
...         print(f"{name} is {age} years old")
...
>>> printUsers(ali=21, mamadreza=18, mahdi=22)
'ali is 21 years old'
'mamadreza is 18 years old'
'mahdi is 22 years old'

>>> print(*[1, 2, 3])
1 2 3
>>> print(*(1, 2, 3))
1 2 3
>>> print(*{'a': 1, 'b': 2, 'c': 3})
a b c

>>> def mean(*numbers):
...     return sum(numbers)/len(numbers)
...
>>> data = [1, 2, 3, 4, 5]
>>> mean(*data)
3.0

>>> def people(**people):
...     for name, job in people.items():
...         print(f'{name} is a {job}')
...
>>> data = {'mohamad': 'teacher', 'samad': 'worker'}
>>> people(**data)
'mohamad is a teacher'
'samad is a worker'