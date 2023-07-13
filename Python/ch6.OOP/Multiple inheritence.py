class Rooster:
  pass

class Hen:
  pass

class Chick(Rooster, Hen):
  pass

class Rooster:
  def name(self):
    print('In Rooster class.')

class Hen:
  def name(self):
    print('In Hen class.')
  def hello(self):
    print('Hello my baby!')

class Chick(Rooster, Hen):
  pass

x = Chick()
x.name()
x.hello()

In Rooster class.
Hello my baby!

class Shape:
    def __init__(self):
        print('Initialize from class Shape')

class Rectangle(Shape):
    def __init__(self):
        print('Initialize from class Rectangle')
        Shape.__init__(self)

class Rhombus(Shape):
    def __init__(self):
        print('Initialize from class Rhombus')
        Shape.__init__(self)

class Square(Rectangle, Rhombus):
    def __init__(self):
        Rectangle.__init__(self)
        Rhombus.__init__(self)

squ = Square()

Initialize from class Rectangle
Initialize from class Shape
Initialize from class Rhombus
Initialize from class Shape

class Shape:
    def __init__(self):
        print('Initialize from class Shape')

class Rectangle(Shape):
    def __init__(self):
        print('Initialize from class Rectangle')
        super().__init__()

class Rhombus(Shape):
    def __init__(self):
        print('Initialize from class Rhombus')
        super().__init__()

class Square(Rectangle, Rhombus):
    def __init__(self):
        super().__init__()

squ = Square()

Initialize from class Rectangle
Initialize from class Rhombus
Initialize from class Shape