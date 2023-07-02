n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(q):
    x, y = map(int, input().split())
    a[x - 1] += y
    cost = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            spray = (a[i - 1] - a[i])
            cost += spray * b[i]
            a[i] += spray
    print(cost)