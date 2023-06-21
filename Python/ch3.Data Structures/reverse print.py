numbers = []

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

# Print the numbers in reverse order
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])