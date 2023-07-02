import sys

# Read input
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate initial scent for each flower and store in a new array s
s = [0] * n
for i in range(1, n):
    if a[i] > a[i-1]:
        s[i] = 1

# Calculate the cumulative sum of b to get prefix sums pb (used later)
pb = [0] * n
pb[0] = b[0]
for i in range(1, n):
    pb[i] = pb[i-1] + b[i]

# Loop over each day's query
for _ in range(q):
    y, x = map(int, input().split())

    # Adjust scent values for flowers affected by the spray on this day
    if y > 1:
        s[y-2] -= x >= a[y-2]
        s[y-2] += x+a[y-2]-y+2 <= a[y-1]

    # Calculate the minimum cost to adjust scents so that all flowers smell sweet again.
    c_min=pb[n - 1]
    
    c_curr=c_min
    
    for i in reversed(range(n - 1)):
        adj_needed=max([s[j + 1]*(j-i) for j in range(i,n - 1)])
            
        if adj_needed>0:
                c_curr+=adj_needed*b[i]+x*adj_needed
                
        else: 
                break
            
        c_min=min(c_min,c_curr)

print(c_min)