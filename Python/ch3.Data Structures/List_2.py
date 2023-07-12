>>> stack = ["first", "second", "third"]
>>> stack
['first', 'second', 'third']
>>> stack.append('fourth')
>>> stack.append('fifth')
>>> stack
['first', 'second', 'third', 'fourth', 'fifth']
>>> stack.pop()
'fifth'
>>> stack
['first', 'second', 'third', 'fourth']

>>> queue = ["ali", "mohammad"]
>>> queue.append("reza") # similar to push
>>> queue.append("amir") 
>>> queue
['ali', 'mohammad', 'reza', 'amir']
>>> queue[0] # similar to top
'ali'
>>> queue.pop(0)
'ali'
>>> queue
['mohammad', 'reza', 'amir']

>>> myList = ['ali', 1, 2, 3, 'chetor']
>>> for it in myList:
...     print(it)
... 
ali
1
2
3
chetor

>>> myList = [0, 1, 2, 3]
>>> for i, it in enumerate(myList):
...     print("the {0}th object in myList is {1}!".format(i+1, it))
... 
the 1th object in myList is 0!
the 2th object in myList is 1!
the 3th object in myList is 2!
the 4th object in myList is 3!

>>> listA = [1, 2, 3, 4]
>>> listB = ['a', 'b', 'c', 'd']
>>> listC = ['I', 'II', 'III', 'IV']
>>> for a, b, c in zip(listA, listB, listC):
...     print("{0}th alphabet or {1} in greece is {2}".format(a, c, b))
... 
1th alphabet or I in greece is a
2th alphabet or II in greece is b
3th alphabet or III in greece is c
4th alphabet or IV in greece is d

>>> ls = [2, 4, 3, 1]
>>> sorted(ls)
[1, 2, 3, 4]

>>> ls = ['a', 'bcd', 'salam', 'hello']
>>> reversed(ls)
<list_reverseiterator object at 0x10a189908>
>>> for i in reversed(ls):
...     print(i, end=' ')
... 
hello salam bcd a

>>> def f(x):
...    return True if x%2 == 0 else False
...
>>> ls = [1, 2, 4, 3, 6, 4]
>>> filter(f, ls)
<filter object at 0x00B77E50>
>>> for x in filter(f, ls):
...     print(x, end=' ')
...
2 4 6 4

>>> def f(x):
...    return int(x)
...
>>> ls = [2, '4', False, 3.14]
>>> map(f, ls)
<map object at 0x00B77F90>
>>> for x in map(f, ls):
...     print(x, end=' ')
...
2 4 0 3
>>> for x in map(int, ls):
...     print(x, end=' ')
...
2 4 0 3

>>> number = map(int, input().split())
1 2 3 4 5
>>> sum(number)
15

>>> ls = [1, 2, 3, 4]
>>> sum(ls)
10
>>> ls = ['a', 'b', 'c', 'd']
>>> sum(ls)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'