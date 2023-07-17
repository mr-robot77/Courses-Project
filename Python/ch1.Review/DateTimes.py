import datetime # for getting time & saving it
from datetime import time # for getting 24-hour time alone

# for create a time object with 4 input : time(Hour,Minutes,Seconds,Microseconds)

>>> from datetime import time
>>> t = time(17, 21, 20, 2021)
>>> t.hour = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: attribute 'hour' of 'datetime.time' objects is not writable
>>> print(t.hour, t.minute, t.second, t.microsecond)
17 21 20 2021
>>> t = time()
>>> print(t.hour, t.minute, t.second, t.microsecond)
0 0 0 0
>>> type(t)
<class 'datetime.time'>
>>> t = time(34, 21)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: hour must be in 0..23

from datetime import date # for getting days

>>> from datetime import date
>>> d = date(2019, 5, 23)
>>> print(d.year, d.month, d.day)
2019 5 23
>>> d.year = 23
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: attribute 'year' of 'datetime.date' objects is not writable
>>> d
datetime.date(2019, 5, 23)
>>> type(d)
<class 'datetime.date'>
>>> d = date(2019, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'day' (pos 3) not found
>>> d = date(2019, 5, 32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: day is out of range for month

# for create date & time

>>> from datetime import datetime
>>> dt = datetime(1, 2, 3, 4, 5, 6, 7)
>>> print(dt.year, dt.month, dt.day)
1 2 3
>>> print(dt.hour, dt.minute, dt.second, dt.microsecond)
4 5 6 7
>>> dt.date()
datetime.date(1, 2, 3)
>>> dt.time()
datetime.time(4, 5, 6, 7)
>>> type(dt)
<class 'datetime.datetime'>
>>> dt
datetime.datetime(1, 2, 3, 4, 5, 6, 7)
>>> dt = datetime(1, 2, 3, 4)
>>> print(dt.hour, dt.minute, dt.second, dt.microsecond)
4 0 0 0

>>> datetime.now()
datetime.datetime(2019, 4, 29, 16, 15, 19, 375528)