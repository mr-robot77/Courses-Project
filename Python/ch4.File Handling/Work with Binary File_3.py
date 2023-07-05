>>> a = bytes([1, 129, 231])
>>> a
b'\x01\x81\xe7'
>>> list(a)
[1, 129, 231]
>>> a[1:3]
b'\x81\xe7'
>>> a = bytes([1, 260])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: bytes must be in range(0, 256)