def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())

# Calculate GCD and LCM
g = gcd(n, m)
l = (n * m) // g

# Print the results
print(g, l)
