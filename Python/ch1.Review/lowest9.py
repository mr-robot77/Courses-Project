import math

def f(n):
    # Calculate n!
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    
    # Find the least significant non-zero digit of n!
    digit = factorial % 10
    while digit == 0:
        factorial //= 10
        digit = factorial % 10
    
    return digit

n = int(input())

if n < 1 or n > 65536:
    print("Error: n is out of range")
else:
    result = f(n)
    print(result)
