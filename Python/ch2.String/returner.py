# Read_input():
k = int(input()) 
code = input()
def locks(char , number):
    position= number.find(char)
    return min(position , len(number)-position)

# Calculate_minimum_turns
minimum_turns = 0
for i in range(k):
    minimum_turns += locks(code[i], input())
print(minimum_turns)
