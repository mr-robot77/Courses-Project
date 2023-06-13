n, q = map(int, input().split())
a = list(map(int, input().split()))

# Calculate the even counts for each number in the array
even_counts = [0] * n
for i in range(n):
    if a[i] % 2 == 0:
        even_counts[i] = 1
    if i > 0:
        even_counts[i] += even_counts[i-1]

# Process the queries
for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        # Update the value of a[x-1]
        a[x-1] = y
        # Update the even count for a[x-1]
        if y % 2 == 0:
            even_counts[x-1] = 1
        else:
            even_counts[x-1] = 0
        # Update the even counts for the rest of the array
        if x > 1:
            even_counts[x-1] += even_counts[x-2]
        for j in range(x, n):
            if a[j] % 2 == 0:
                even_counts[j] = even_counts[j-1] + 1
            else:
                even_counts[j] = even_counts[j-1]
    elif t == 2:
        # Check if all numbers in the range [x-1, y-1] appear an even number of times
        even_count = even_counts[y-1]
        if x > 1:
            even_count -= even_counts[x-2]
        if (y-x+1) % 2 == 0 and even_count == (y-x+1)//2:
            print("YES")
        elif (y-x+1) % 2 == 1 and even_count == (y-x+1)//2 + 1:
            print("YES")
        else:
            print("NO")
