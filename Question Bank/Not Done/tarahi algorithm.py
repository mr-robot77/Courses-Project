n = int(input())
a = [(int(x), i) for i, x in enumerate(input().split())]
b = [(int(x), i) for i, x in enumerate(input().split())]

a.sort(key=lambda x: x[0], reverse=True)
b.sort(key=lambda x: x[0], reverse=True)

chosen = [False] * n
ans = 0
j = 0
for i in range(n):
    if i % 2 == 0:
        while chosen[a[j][1]]:
            j += 1
        chosen[a[j][1]] = True
        j += 1
    else:
        while chosen[b[j][1]]:
            j += 1
        ans += b[j][0]
        chosen[b[j][1]] = True
        j += 1

print(ans)