names = dict()
cnt = int(input())
for i in range(cnt):
    name, family = input().split()
    names[name] = names.get(name, 0) + 1
print(max(names.values()))