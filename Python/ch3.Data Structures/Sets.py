>>> type(set())
<class 'set'>
>>> st = {2, 3, 1}
>>> st
{1, 2, 3}
>>> len(st)
3
>>> type(st)
<class 'set'>
>>> st = {}
>>> type(st)
<class 'dict'>

>>> names = set()
>>> names.add('ali')
>>> names.add('mohamadreza')
>>> names.add('amir')
>>> names.add('amir')
>>> names
{'amir', 'mohamadreza', 'ali'}

>>> nums = set()
>>> nums.add(1)
>>> nums.add(2)
>>> nums.add(3)
>>> 1 in nums
True
>>> 4 in nums
False

>>> a = {1, 2, 3}
>>> a.remove(1)
>>> a.discard(2)
>>> a
{3}
>>> a.discard(4)
>>> a.remove(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4

>>> a = {1, 2, 3}
>>> b = {3, 2, 4}
>>> a.intersection(b)
{2, 3}
>>> b.intersection(a)
{2, 3}
>>> a & b
{2, 3}
>>> b.union(a)
{1, 2, 3, 4}
>>> a | b
{1, 2, 3, 4}

>>> a = {1, 2, 3}
>>> b = {3, 2, 4}
>>> a.difference(b)
{1}
>>> b - a
{4}
>>> a ^ b
{1, 4}
>>> b.symmetric_difference(a)
{1, 4}

>>> a = set("salam")
>>> b = set("varam")
>>> {x for x in a if x not in b}
{'s', 'l'}