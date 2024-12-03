# Step 1: Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

safe_lines = 0  # Counter for safe reports

# Step 2: Iterate through each report
for line in lines:
    # Parse the levels as integers
    levels = list(map(int, line.split()))
    
    # Step 3: Check differences
    differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        continue  # Skip this report if any difference is out of range

    # Step 4: Check monotonicity
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        safe_lines += 1  # Count this report as safe

# Step 5: Print the result
print(f'Number of safe lines: {safe_lines}')
