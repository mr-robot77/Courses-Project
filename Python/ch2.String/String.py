s = "Hello "
t = '!'
name = input()
print(s + name + t)

>>> s = 'salam'
>>> t = 'ali'
>>> s + t
'salamali'
>>> s * 3
'salamsalamsalam'
>>> 'ai' in s
False
>>> 'al' in s
True
>>> 'ai' not in s
True
>>> 'al' not in s
False

>>> s = 'mokar'
>>> s[0]
m
>>> s[2]
k
>>> s[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[0] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> s = 'salam'
>>> s[1:4]
'ala'
>>> s[1:]
'alam'
>>> s[:3]
'sal'
>>> s[4:3]
''
>>> s[:]
'salam'
>>> s[-3:-1]
'la'
>>> s[-3:]
'lam'
>>> s[:-1]
'sala'
>>> s[-3:4]
'la'
>>> s[-4:3]
'al'

>>> 'Ali23'.lower()
'ali23'
>>> 'Ali23'.upper()
'ALI23'
>>> 'Ali23'.isalpha()
False
>>> 'Ali'.isalpha()
True
>>> 'Ali23'.isdigit()
False
>>> '23'.isdigit()
True
>>> 'Ali23'.zfill(2)
'Ali23'
>>> 'Ali23'.zfill(8)
'000Ali23'

>>> 'ahmad'.count('ma')
1
>>> 'ahmad'.count('ali')
0
>>> 'aaaa'.count('aa')
2
>>> 'ahmad'.find('ali')
-1
>>> 'ahmad'.find('ma')
2
>>> 'Hello world!'.split(' ')
['Hello', 'world!']
>>> 'Hello world!'.split('l')
['He', '', 'o wor', 'd!']
>>> 'Hello world!'.replace('l', 'salam!')
'Hesalam!salam!o worsalam!d!'
>>> 'Hello world!'.replace('h', 'salam!')
'Hello world!'
>>> 'HeLLo'.replace('LL', 'll')
Hello

>>> s = "ali"
>>> len(s)
3
>>> len("salam")
5

>>> s = 'mokar'
>>> s.replace('m', 'l').upper()
LOKAR
>>> s
mokar
>>> s = s.replace('m', 'l').upper()
>>> s
LOKAR

>>> s = 'spartacus'
>>> s.removeprefix('s')
'partacus'
>>> s.removeprefix('spar')
'tacus'
>>> s.removeprefix('part')
'spartacus'
>>> s.removesuffix('s')
'spartacu'
>>> s.removesuffix('acus')
'spart'
>>> s.removesuffix('tacu')
'spartacus'