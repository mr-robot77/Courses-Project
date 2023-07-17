class First:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

>>> from main import First
>>> obj1 = First(42)
>>> obj2 = First(4711)
>>> obj1.get_x()
42
>>> obj1.set_x(50)
>>> obj1.get_x()
50

>>> obj1.set_x(obj1.get_x()+obj2.get_x())
>>> obj1.get_x()
4761

class Second:

    def __init__(self, x):
        self.x = x

>>> from main import Second
>>> obj1 = Second(42)
>>> obj2 = Second(4711)
>>> obj1.x
42
>>> obj1.x = 43
>>> obj1.x = obj1.x + obj2.x
>>> obj1.x
4754

class First:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

>>> from main import First
>>> obj1 = First(1001)
>>> obj1.get_x()
1000
>>> obj2 = First(15)
>>> obj2.get_x()
15
>>> obj3 = First(-1)
>>> obj3.get_x()
0

class Second:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        print("---> getter <---")
        return self.__x

    @x.setter
    def x(self, x):
        print("---> setter <---")
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


>>> from main import Second
>>> obj1 = Second(1001)
---> setter <---
>>> obj1.x
---> getter <---
1000
>>> 
>>> 
>>> obj2 = Second(-73)
---> setter <---
>>> obj2.x
---> getter <---
0
>>> 
>>> 
>>> obj3 = Second(17)
---> setter <---
>>> obj3.x
---> getter <---
17
>>> obj3.x = 25
---> setter <---
>>> obj3.x
---> getter <---
25

class First:

    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)


class First:

    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)

class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 

Wall_E= Robot("Wall-E", 1979, 0.2, 0.4 )
Hal = Robot("Hal", 1993, -0.4, 0.3)
print(Wall_E.condition)
print(Hal.condition)

# output
# Seems to be okay!
# I feel bad!