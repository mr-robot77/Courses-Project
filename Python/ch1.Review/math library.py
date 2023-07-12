import math

ceil(x)
floor(x)
fabs(x)
factorial(x)
gcd(x,y)

pow(x,y)
log(x)
log(x,b)
sqrt(x)

sin(x)
cos(x)
tan(x)
asin(x)
acos(x)
atan(x)
degrees(x)
radians(x)

pi
e
tau
inf

#example

import math
x = int(input())
y = math.floor(math.pow(math.e, math.asin(math.pow(math.cos(math.radians(x)), 2))))
print(math.gcd(x, y))