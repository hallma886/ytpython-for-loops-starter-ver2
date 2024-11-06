# Matthew Hall
# 4 November 2024
# Python: The range() Function

# Counting Up & Down
# num = int(input('Please enter an integer: \n'))
# num_2 = num + 1
# print()
# for n in range(1, num_2):
#     print(n)
# print()
# for x in range(num, 0, -1):
#     print(x)
# if x == 1:
#     print('We have lift off!')
# Number Cubes
# for y in range(1,10):
#     print(f'The cube of {y} is {y**3}')
# print()
# Multiplication Table
# number = 7 
# for i in range(1, 101):
#     result = number * i
#     print(f'{number} * {i} = {result}')
# List Iteration
total = 0
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num_elements = len(my_list)
for z in range(num_elements):
    total = total + my_list[z]

print(f'The sum of the prices in our list is: {total}')
print(sum(my_list))





















