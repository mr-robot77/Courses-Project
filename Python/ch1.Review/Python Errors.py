# syntax errors
>>> while True print('Hello World!')
  File "<stdin>", line 1
    while True print('Hello World!')
                   ^
SyntaxError: invalid syntax 

print("salam")
    x = 2
print(x)

  File "a.py", line 2
    x = 2
    ^
IndentationError: unexpected indent

# Exception

>>> x = 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> print(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> z = int('salam')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'salam'

# Exception Management

try:
    x = int(input())
    print("It's a number!")
except:
    print("It's just a string!")