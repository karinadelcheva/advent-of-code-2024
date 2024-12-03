# Step 1: Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

safe_lines = 0  # Counter for safe reports
def is_safe_with_one_failure(levels):
    # Step 1: Calculate differences
    differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]

    # Step 2: Identify invalid differences
    invalid_indices = [i for i, diff in enumerate(differences) if not (1 <= abs(diff) <= 3)]

    # Step 3: Allow at most one invalid difference
    if len(invalid_indices) > 1:
        return False  # More than one failure means unsafe

    # Step 4: If no invalid differences, check monotonicity
    if len(invalid_indices) == 0:
        return all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)

    # Step 5: Handle single invalid difference
    # Remove the invalid difference and check monotonicity
    idx = invalid_indices[0]
    modified_levels = levels[:idx] + levels[idx + 1:]  # Skip the invalid pair
    modified_differences = [modified_levels[i] - modified_levels[i + 1] for i in range(len(modified_levels) - 1)]

    return all(diff > 0 for diff in modified_differences) or all(diff < 0 for diff in modified_differences)

safe_lines = 0

# Step 2: Iterate through each report
for line in lines:
    # Parse the levels as integers
    levels = list(map(int, line.split()))

    if is_safe_with_one_failure(levels):
        safe_lines += 1
        
# Step 5: Print the result
print(f'Number of safe lines: {safe_lines}')
