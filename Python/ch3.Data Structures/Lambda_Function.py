# lambda argumets:expression

>>> (lambda x: x * x)(2)
4
>>> power_two = lambda x: x * x
>>> power_two(2)
4
>>> average = lambda a, b: (a + b) / 2
>>> average(20, 18)
19.0
>>> statistic = lambda a, b: [(a + b) / 2, max(a, b)]
>>> statistic(20, 18)
[19.0, 20]

>>> mylist = [(1,3),(4,5),(2,10),(9,6)]

>>> mylist.sort()
>>> mylist
[(1, 3), (2, 10), (4, 5), (9, 6)]

>>> mylist.sort(key = lambda x: x[-1])
>>> mylist
[(1, 3), (4, 5), (9, 6), (2, 10)]

>>> def myfunc(n):
          return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> mytripler = myfunc(3)
>>> 
>>> mydoubler(11)
22
>>> mytripler(11)
33