>>> dict = {"ali": 12, "amir": 2.3}
>>> dict
{'ali': 12, 'amir': 2.3}
>>> dict['ali']
12
>>> dict['ali'] = 23
>>> dict
{'ali': 23, 'amir': 2.3}
>>> list(dict)
['ali', 'amir']

>>> dict()
{}
>>> dict([("ali", 12), ("amir", 2.3)])
{'ali': 12, 'amir': 2.3}

>>> age = {'mohamadreza':17}
>>> age['ali'] = 22
>>> age['mohamadreza'] = 18
>>> age
{'mohamadreza': 18, 'ali': 22}

>>> square = {1: 1, 2: 4, 3: 9, 4: 16}
>>> 3 in square
True
>>> square[3]
9
>>> 5 in square
False
>>> square[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5

>>> square = {1: 1, 2: 4, 3: 9, 4: 16}
>>> square.pop(3)
9
>>> del square[1]
>>> square
{2: 4, 4: 16}
>>> square.pop(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5

>>> grade = {'mamad': 20, 'ali':19, 'pooyan':19}
>>> grade.get('ali')
19
>>> grade['mahdi'] = grade.get('mahdi', 19) + 1 
>>> grade.get('mahdi')
20

>>> age = {'ali': 21, 'mmdreza': 18, 'mahdi': 22, 'pooyan':25}
>>> type(age.values())
<class 'dict_values'>
>>> type(age.keys())
<class 'dict_keys'>
>>> age.values()
dict_values([21, 18, 22, 25])
>>> list(age.values())
[21, 18, 22, 25]
>>>

>>> {x:x*x for x in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

>>> dict(ali=12, amir=2.3)
{'ali': 12, 'amir': 2.3}

>>> d = {'ali': 'A', 'amir': 'B'}
>>> for k, v in d.items():
...     print(k + " got " + v)
... 
ali got A
amir got B