import re

def parse_instructions(corrupted_memory):
    """
    Parse multiplication instructions with do/don't state control.
    
    Args:
        corrupted_memory (str): Input string containing corrupted memory data
    
    Returns:
        int: Sum of all enabled multiplication results
    """
    # Pattern for multiplications
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    # Patterns for control instructions
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'  # Changed back to don't()
    
    # Find all instructions with their positions
    instructions = []
    
    # Find multiplications
    for match in re.finditer(mul_pattern, corrupted_memory):
        instructions.append({
            'type': 'mul',
            'position': match.start(),
            'nums': (int(match.group(1)), int(match.group(2)))
        })
    
    # Find do() instructions
    for match in re.finditer(do_pattern, corrupted_memory):
        instructions.append({
            'type': 'do',
            'position': match.start()
        })
    
    # Find don't() instructions
    for match in re.finditer(dont_pattern, corrupted_memory):
        instructions.append({
            'type': 'dont',
            'position': match.start()
        })
    
    # Sort instructions by position
    instructions.sort(key=lambda x: x['position'])
    
    # Process instructions in order
    total = 0
    enabled = True  # Multiplications start enabled
    
    for instruction in instructions:
        if instruction['type'] == 'do':
            enabled = True
            print(f"Position {instruction['position']}: Enabled multiplications")
        elif instruction['type'] == 'dont':
            enabled = False
            print(f"Position {instruction['position']}: Disabled multiplications")
        elif instruction['type'] == 'mul' and enabled:
            num1, num2 = instruction['nums']
            result = num1 * num2
            total += result
            print(f"Position {instruction['position']}: Computing {num1} * {num2} = {result} (enabled)")
        elif instruction['type'] == 'mul' and not enabled:
            num1, num2 = instruction['nums']
            print(f"Position {instruction['position']}: Skipping {num1} * {num2} (disabled)")
    
    return total

# Test the function with the example input
# test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# total = parse_instructions(test_input)
with open('input.txt', 'r') as file:
    corrupted_memory = file.readlines()
print(f"Input of {len(corrupted_memory)} lines")
total = 0
for line in corrupted_memory:
    total += parse_instructions(line)
print(f"Total sum: {total}")
