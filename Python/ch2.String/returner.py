# Read_input():
k = int(input()) 
code = input()
locks = []
for i in range(k):
    locks.append(list(map(int,input().split())))  

# Calculate_minimum_turns
minimum_turns = 0   
for i in range(k):
    number = int(code[i])
    position = 0
    if number in locks[i]:
        position = locks[i].index(number)
        minimum_turns += abs(position - int(locks[i][0]))
print(minimum_turns)