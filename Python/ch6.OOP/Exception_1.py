# Exception Handling
try:
    x = int(input())
    print("It's a int number!")
except:
    print("It's not a int number!")

>>> int(input())
'Quera'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Quera'
>>> 

>>> for i in range(3):
...     try:
...         if i == 0:
...             1/0
...         if i == 1:
...             int("salam")
...         if i == 2:
...             "salam" + 1
...     except ZeroDivisionError:
...         print("ZeroDivisionError called") # 1/0
...     except TypeError:
...         print("TypeError called") # "salam" + 1
...     except ValueError:
...         print("ValueError called") # int("salam")
...

ZeroDivisionError called
ValueError called
TypeError called

>>> for i in range(3):
...     try:
...             if i == 0:
...                     1/0
...             if i == 1:
...                     int("salam")
...             if i == 2:
...                     "salam" + 1
...     except (ZeroDivisionError, TypeError, ValueError):
...             print("an error occurred")
... 

an error occurred
an error occurred
an error occurred