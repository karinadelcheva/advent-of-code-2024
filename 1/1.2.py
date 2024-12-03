from collections import Counter

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

# Step 3: Count occurrences in the right list
right_counts = Counter(right_list)

# Step 4: Calculate the similarity score
similarity_score = 0
for num in left_list:
    similarity_score += num * right_counts[num]

# Step 5: Print the result
print(f'Similarity score: {similarity_score}')