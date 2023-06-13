d = int(input())
p = int(input())
i =1
while True:
    s=i*d
    r=s%p
    if 0 <=r and r<=p/2:
        print(s)
        break
    i+=1
