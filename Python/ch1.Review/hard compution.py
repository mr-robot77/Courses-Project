from math import *
x = int(input())
y = ceil(pow(x,5/3)+tan(radians(x)))
z = floor(pow(pi, 2+atan(pow(sin(radians(x)),2))))
print(gcd(y, z))
