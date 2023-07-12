while condition:
    # statements
    pass

a = 0
b = 1
while a < 10:
    print(a)
    c = b
    b = a + b
    a = c

# continue statement

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# break statement

result = 0
while True:
    n = int(input())
    if n == 0:
        break
    result = result + n
print(result)

x = 0
while True:
    x += 1
    if x == 20:
        break
    if x % 2 == 0:
        continue
    print(x)


# for loop

for iterator in iterable:
    # statements
    pass

# for example

numbers = [1, 2, 3]

for num in numbers:
    print(num)

1
2
3

# another for example

words = [['s', 'a', 'l', 'a', 'm'], ['k', 'h', 'o', 'o', 'b', 'i', '?']]

for word in words:
    for char in word:
        print(char, end='')
    print()

salam
khoobi?

# range function

for i in range(5):
    print(i, end=' ')

print()

for i in range(5, 10):
    print(i, end=' ')

print()

for i in range(0, 10, 2):
    print(i, end=' ')

0 1 2 3 4
5 6 7 8 9
0 2 4 6 8

words = ['salam', 'khoobi?', 'na']

for i in range(len(words)):
    print(words[i])

for i in range(0, len(words), 2):
    print(" *** " + words[i])

salam
khoobi?
na
 *** salam
 *** na