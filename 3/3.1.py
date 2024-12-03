import re

def parse_multiplications(corrupted_memory):
    # Pattern matches mul(X,Y) where X and Y are 1-3 digits with no spaces
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches in the input string
    matches = re.finditer(pattern, corrupted_memory)
    
    total = 0
    for match in matches:
        # Extract the two numbers from each match
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        
        # Multiply and add to total
        result = num1 * num2
        # print(f"Found multiplication: {num1} * {num2} = {result}")
        total += result
        
    return total

# Test the function with the example input
# test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open('input.txt', 'r') as file:
    corrupted_memory = file.readlines()
print(f"Input of {len(corrupted_memory)} lines")
total = 0
for line in corrupted_memory:
    total += parse_multiplications(line)
print(f"Total sum: {total}")
