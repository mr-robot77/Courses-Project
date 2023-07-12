>>> class Course:
...     def __init__(self, title, price):
...         self.title = title
...         self.price = price
...     def introduction(self):
...         return f'This is a {self.title} Course!'
...
>>> ali = Account('Ali Safinal', 'safinal', '@Li2001')
>>> math = Course('Math with salib', 50000)
>>> ali.full_name
'Ali Safinal'
>>> math.full_name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Course' object has no attribute 'full_name'
>>> math.introduction()
'This is a Math with salib Course!'
>>> ali.introduction()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Account' object has no attribute 'introduction'