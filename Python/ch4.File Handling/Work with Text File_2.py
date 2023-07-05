# Reading Lines of File
f = open("Info.txt", "r")
lines = []
while True:
    line = f.readline()
    if line == '':
        break # end of file
    lines.append(line)
lines.reverse()
for line in lines:
    print(line, end = '')