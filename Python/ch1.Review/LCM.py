p, d = input().split()
p = int(p)
d = int(d)
while p !=d:
	if p>d:
		p=p-d
	else:
		d=d-p
lcm=(p*d)/p
print(lcm)