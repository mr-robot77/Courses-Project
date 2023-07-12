>>> walrus = False
>>> print(walrus)
False

# assignment method example-1

>>> print(walrus := True)
True

inputs = list()
while True:
    current = input()
    if current == "quit":
        break
    inputs.append(current)


# assignment method example-2

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)