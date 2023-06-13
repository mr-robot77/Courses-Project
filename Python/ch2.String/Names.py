def count_unique_chars(s):
    return len(set(s))

n = int(input())
names = []

for _ in range(n):
    name = input()
    names.append(name)

max_unique_chars = max([count_unique_chars(name) for name in names])

print(max_unique_chars)