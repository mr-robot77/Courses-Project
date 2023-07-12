def function(arg1, arg2, ...):
    # statments and return
    pass

>>> def f(n):
...     return n+n
... 
>>> f(2)
4
>>> f('2')
'22'

>>> def f(a):
...     return a
... 
>>> f(10)
10
>>> g = f
>>> g(10)
10
>>> type(g)
<class 'function'>
>>> f(f(10))
10
>>> f(f)(10)
10