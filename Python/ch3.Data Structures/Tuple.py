>>> t = ("ali", 123, 2.5)
>>> t
('ali', 123, 2.5)
>>> type(t)
<class 'tuple'>

>>> t = ("ali", 123, 2.5)
>>> t[0]
'ali'
>>> t[0:2]
('ali', 123)
>>> for it in t:
...     print(it)
... 
ali
123
2.5

>>> t = "ali", 123, 2.5
>>> t
('ali', 123, 2.5)
>>> type(t)
<class 'tuple'>

>>> a, b, c = 10, 20, 30
>>> a
10
>>> b
20
>>> c
30
>>> a, b = b, a
>>> a
20
>>> b
10

>>> t = ()
>>> len(t)
0
>>> type(t)
<class 'tuple'>
>>> t = (1)
>>> type(t)
<class 'int'>
>>> t = 1,
>>> len(t)
1
>>> type(t)
<class 'tuple'>

>>> myList = [1, 2]
>>> def f():
...     return myList
... 
>>> a = f()
>>> a.append("12")
>>> myList
[1, 2, '12']
>>> a[0] = 10
>>> myList
[10, 2, '12']

>>> myTuple = 1, 2
>>> def f():
...     return myTuple
... 
>>> a = f()
>>> a
(1, 2)
>>> a[0] = 10
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a = 3, 4
>>> myTuple
(1, 2)