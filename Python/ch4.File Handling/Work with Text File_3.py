# Writing in File
n = int(input())
f = open("dst.txt", "w")
for i in range(n):
    line = input()
    f.write(line + '\n')