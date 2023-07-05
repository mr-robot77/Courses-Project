>>> a = b'\x02\xA1\x80'
>>> a
b'\x02\xa1\x80'
>>> a[0]
2
>>> a[1]
161
>>> a[2]
128
>>> a[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index out of range
>>> type(a)
<class 'bytes'>
>>> list(a)
[2, 161, 128]