s = input()
stack = []

for c in s:
    if c == '=':
        if stack:
            stack.pop()
    else:
        stack.append(c)

print(''.join(stack))