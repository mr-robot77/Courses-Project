>>> raise NameError('salam')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: salam

raise ValueError # 'raise ValueError()'

>>> try:
...     raise NameError('salam')
... except NameError:
...     print('an exception raised')
...     raise
... 
an exception raised
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
NameError: salam

# Define Exception

>>> class A(Exception):
...     pass
... 
>>> class B(A):
...     pass
... 
>>> class C(B):
...     pass
>>> try:
...     raise C
... except A as e:
...     print('exception found', type(e))
... 
exception found <class '__main__.C'>

try:
    run_testcase(case)
except Exception:
    tests_failed += 1
    print('F', end='')
else:
    test_passed +=1
    print('P', end='')

try:
    1/0
except:
    print('error!!')
    raise
finally:
    print('finally is running')


error!!
finally is running
Traceback (most recent call last):
File "a.py", line 2, in <module>
1/0
ZeroDivisionError: division by zero

# Exception Handling Structure:

try:
	# Run this code
except as :
	# Execute this code when
	# there is an exception
else:
	# No exceptions? Run this code.
finally:
	# Always run this code