def f(n):
    yield n//1
    yield n//2
    yield n//3

div = f(6)
print(type(div))
print(div)
print(list(div))

<class 'generator'>
<generator object f at 0x7f6254849a40>
[6, 3, 2]

def myRange(l, r, step=1):
    while l < r:
        yield l
        l += step
    return 0
    yield 0

>>> for i in myRange(1, 10, 3):
...     print(i, end=' ')
1 4 7
>>> list(myRange(1, 20, 4))
[1, 5, 9, 13, 17]