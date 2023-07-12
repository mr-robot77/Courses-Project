>>> myList = [10, 20, 30]
>>> myList
[10, 20, 30]

zeros = [0] * 100

>>> myList = [10, 20, 30]
>>> myList
[10, 20, 30]
>>> myList[:]
[10, 20, 30]
>>> myList[1]
20
>>> myList[1:]
[20, 30]
>>> myList[:1]
[10]
>>> myList[1:0]
[]
>>> myList[0:2]
[10, 20]

>>> num = [10, 20, 30]
>>> num[0] = 1
>>> num
[1, 20, 30]
>>> num[0:3] = [1, 2, 3]
>>> num
[1, 2, 3]

>>> main = [1, 2, 3]
>>> ref = main
>>> ref
[1, 2, 3]
>>> main[0] = 10
>>> ref
[10, 2, 3]
>>> ref[0] = 1
>>> main
[1, 2, 3]
>>>

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list((10, 20, 30))
[10, 20, 30]
>>> list("salam")
['s', 'a', 'l', 'a', 'm']

>>> myList = [10]
>>> myList.append(20)
>>> myList
[10, 20]
>>> myList.append(30)
>>> myList.append(40)
>>> myList
[10, 20, 30, 40]

>>> myList = [10]
>>> myList.extend([20, 30, 40])
>>> myList
[10, 20, 30, 40]

>>> myList = [10, 20]
>>> myList.insert(1, 15)
>>> myList
[10, 15, 20]
>>> myList.insert(0, 5)
>>> myList
[5, 10, 15, 20]
>>> myList.insert(4, 25)
>>> myList
[5, 10, 15, 20, 25]

>>> myList = [10, 20, 20]
>>> myList.remove(20)
>>> myList
[10, 20]
>>> myList.remove(30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

>>> myList = [10, 20, 30]
>>> myList.pop(0)
10
>>> myList
[20, 30]
>>> myList.pop()
30
>>> myList
[20]

>>> myList = [10, 20, 20]
>>> myList.clear()
>>> myList
[]
>>> myList = [10, 20, 20]
>>> del myList[:]
>>> myList
[]

>>> myList = ["amir", "ali", "amir", "ali"]
>>> myList.index('ali')
1
>>> myList.index('ali', 2, 4)
3
>>> myList.index('ali', 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'ali' is not in list

>>> myList = ["amir", "ali", "amir", "ali"]
>>> myList.count('ali')
2
>>> myList.count('mohamadreza')
0

>>> companies = ['apple', 'samsung', 'xiaomi', 'sony', 'nokia']
>>> companies
['apple', 'samsung', 'xiaomi', 'sony', 'nokia']
>>> companies.sort()
>>> companies
['apple', 'nokia', 'samsung', 'sony', 'xiaomi']
>>> def getLength(a):
...     return len(a)
... 
>>> companies.sort(key=getLength)
>>> companies
['sony', 'apple', 'nokia', 'xiaomi', 'samsung']

>>> numbers = [1, 2, 3, 4, 5]
>>> numbers.reverse()
>>> numbers
[5, 4, 3, 2, 1]

>>> names = ['ali', 'mohamadreza', 'mahdi']
>>> ' '.join(names)
'ali mohamadreza mahdi'
>>> '/'.join(['home', 'lib', 'python.py'])
'home/lib/python.py'

>>> numbers = [1, 2, 3, 4, 5]
>>> numbers.copy()
[1, 2, 3, 4, 5]
>>> numbers[:]
[1, 2, 3, 4, 5]