>>> age = 12
>>> height = 178.5
>>> isMale = True
>>> f'Age : {age}, Height : {height}, Gender : {isMale}'
'Age : 12, Height : 178.5, Gender : True'

>>> variable = 5
>>> f"{variable=}"
'variable=5'

greeting = "Hello %s!"
name = input("Please enter your name:\n")
print(greeting % name)

greeting = "Hello %s with %d years old!"
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
print(greeting % (name, age))

greeting = "Hello {} with {} years old!"
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
print(greeting.format(name, age))

>>> "{:+} {:+} {:+}".format(241.1, -124.21, 0)
'+241.1 -124.21 +0'
>>> "{:.3f} {:.3f}".format(122, 33.22191)
'122.000 33.222'
>>> "{:b} {:b}".format(-34, 21)
'-100010 10101'
>>> "{:x} {:x}".format(241, 124)
'f1 7c'
>>> "{:o} {:o}".format(241, 124)
'361 174'
>>> "{:0=8} {:1=8} {:2=2}".format(12, 21.12, 312)
'00000012 11121.12 312'

>>> "Hello {0} with {1} years old!".format("Ali", "23")
'Hello Ali with 23 years old!'
>>> "Hello {name} with {age} years old!".format(name = "Ali", age = "23")
'Hello Ali with 23 years old!'
>>> "Hello {0} with {age} years old!".format("Ali", age = "23")
'Hello Ali with 23 years old!'

>>> "{0:.3f} {0:+}".format(23.12)
'23.120 +23.12'
>>> "{num:.3f} {num:+}".format(num=23.12)
'23.120 +23.12'