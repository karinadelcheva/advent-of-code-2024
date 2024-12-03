# Step 1: Open and read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Parse the input into two separate lists
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())  # Split each line into two integers
    left_list.append(left)
    right_list.append(right)

# Step 3: Sort both lists
left_list.sort()
right_list.sort()

# Step 4: Calculate the total distance
total_distance = 0
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)  # Calculate absolute difference and sum it up

# Step 5: Print the result
print(f'Total distance between the lists: {total_distance}')

