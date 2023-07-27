class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

>>> favorite_movie = Movie('Fight Club', 1999)
>>> dir(favorite_movie)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'release_year']

>>> print(favorite_movie)
<__main__.Movie object at 0x0000023C8E1B0F70>

# dunder method __str__

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self):
        return self.name

>>> favorite_movie = Movie('Fight Club', 1999)
>>> favorite_movie.__str__()
'Fight Club'
>>> str(favorite_movie)
'Fight Club'
>>> print(favorite_movie)
Fight Club

>>> hangover = Movie('Hangover', 2009)
>>> se7en = Movie('ُSe7en', 1995)
>>> se7en < hangover
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Movie' and 'Movie'

# dunder method __lt__

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self):
        return self.name

    def __lt__(self, other_object):
        return self.release_year < other_object.release_year 

>>> hangover = Movie('Hangover', 2009)
>>> se7en = Movie('ُSe7en', 1995)
>>> se7en.__lt__(hangover)
True
>>> se7en < hangover
True
>>> hangover.__lt__(se7en)
False
>>> hangover < se7en
False

>>> scarface = Movie('Scarface', 1983)
>>> scarface()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Movie' object is not callable

# dunder method __call__

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self):
        return self.name

    def __lt__(self, other_object):
        return self.release_year < other_object.release_year 

    def __call__(self):
        return 'Say Hello to My Little Friend!😈'

>>> scarface = Movie('Scarface', 1983)
>>> scarface.__call__()
'Say Hello to My Little Friend!😈'
>>> scarface()
'Say Hello to My Little Friend!😈'