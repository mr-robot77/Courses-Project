def print_test():
    print("test file")

class Test:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(self.x)

a = 10

import test
test.print_test()
x = test.Test(4)
x.print()
print(test.a)

test file
4
10

>>> import test
>>> test.a
10
>>> test.print_test()
test file
>>> test.Test
<class 'test.Test'>
>>> type(test)
<class 'module'>

>>> test.a = 20
>>> test.a
20
>>> test = 4
>>> test.print_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'test_print'
>>> import test
>>> test.a
20

# import a file from another place

>>> import main.test
>>> main.test.a
10
>>> main.test.print_test()
test file
>>> type(main.test)
<class 'module'> 

# using "from" keyword for one attribute from a module

>>> from test import a
>>> a
10
>>> from test import print_test , Test
>>> print_test()
test file
>>> type(Test)
<class 'type'>

# using "from" keyword for all attribute from a module with * char

>>> from math import *
>>> cos(pi)
-1.0
>>> sin(pi/2)
1.0

# using "as" keyword for one attribute from a module with different name

>>> from math import sin as cos
>>> from math import cos as sin
>>> from math import pi as p
>>> sin(p)
-1.0
>>> cos(p/2)
1.0