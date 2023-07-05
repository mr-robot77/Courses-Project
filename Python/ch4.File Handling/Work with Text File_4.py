# File Pointer
>>> f = open("test.txt", "w")
>>> f.tell()
0
>>> f.write("salam")
5
>>> f.tell()
5
>>> f.write("ali")
3
>>> f.tell()
8

f = open("a.txt", "r")
l, r = (int(x) for x in input().split())
f.seek(l)
s = f.read(r - l + 1)
print(s)