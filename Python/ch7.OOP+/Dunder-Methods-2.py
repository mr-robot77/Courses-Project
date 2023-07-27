# dunder method __add__

class FootballTeam:
    def __init__(self, name, cups_number):
        self.name = name
        self.cups_number = cups_number

    def __add__(self, other_object):
        return self.cups_number + other_object.cups_number

>>> bayern_munich = FootballTeam('FC Bayern Munich', 6)
>>> barcelona = FootballTeam('FC Barcelona', 5)
>>> bayern_munich + barcelona
11

# dunder method __len__

class CustomList(list):
    def __len__(self):
        return len(set(self))

>>> my_list = CustomList([1, 1, 1, 1, 1, 684])
>>> my_list.__len__()
2
>>> len(my_list)
2

# dunder methods __iter__ and __next__

>>> ls = [1, 2, 3]
>>> it = iter(ls)
>>> it
<list_iterator object at 0x10ce60940>
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration

import random

class RandomShuffle:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration

        index = random.randint(0, len(self.data)-1)
        index = int(index)
        return self.data.pop(index)

number = [1, 2, 3, 4, 5, 6]
number_random = RandomShuffle(number)

print(*number)
print(*number_random)

1 2 3 4 5 6
6 5 2 1 3 4