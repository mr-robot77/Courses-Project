def calculator(n, m, ls):
   groups = [ls[i:i+m] for i in range(0, n, m)]  # Dividing the list into groups of size m
   new_list = [sum(group) for group in groups]  # Creating a new list with sums of each group
   
   total_value = sum(new_list[::2]) - sum(new_list[1::2])  # Calculating the final value by alternating addition and subtraction
   
   return total_value

# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
