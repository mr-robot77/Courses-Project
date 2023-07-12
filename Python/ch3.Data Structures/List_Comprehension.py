>>> sq = []
>>> for x in range(10):
...     sq.append(x*x)
... 
>>> sq
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> sq = [x*x for x in range(10)]
>>> sq
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> [0 for x in range(5)]
[0, 0, 0, 0, 0]

>>> [str(x)+y for x in [1, 2, 3] for y in ['A', 'B']]
['1A', '1B', '2A', '2B', '3A', '3B']

>>> [(x, y) for x in [1, 2, 3] for y in [1, 2, 3] if x != y]
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

>>> data = [10, -4, 53, 122, 0]
>>> [x for x in data if x > 0]
[10, 53, 122]
>>> [x*x for x in data]
[100, 16, 2809, 14884, 0]
>>> [x*x, x for x in data]
File "<stdin>", line 1
[x*x, x for x in data]
^
SyntaxError: invalid syntax

>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> for i in range(3):
...    for j in range(3):
...        print(matrix[i][j], end=' ')
...    print()
...
1 2 3
4 5 6
7 8 9

>>> zeros = [[0 for c in range(m)] for r in range(n)]

>>> a = ['ali', 'rafte', 'key', 'barmigarde?']
>>> del a[0]
>>> a
['rafte', 'key', 'barmigarde?']
>>> del a[0:2]
>>> a
['barmigarde?']
>>> del a[:]
>>> a
[]

>>> name = "salam"
>>> name
'salam'
>>> del name
>>> name
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined

>>> ls = [0, 1, 2, 3, 4]
>>> print(*ls)
0 1 2 3 4