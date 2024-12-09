# --- Part Two ---
# While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

# For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.
# After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

# Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?



def get_middle_page(sequence):
    index = (len(sequence) - 1) // 2  # Lower middle for even lengths
    return sequence[index]


ordering_rules = set()
sequences = []
with open('input.txt', 'r') as file:
    # Read ordering rules
    for line in file:
        line = line.strip()
        if not line:
            break  # Empty line indicates end of ordering rules
        if '|' in line:
            x, y = line.strip().split('|')
            ordering_rules.add((int(x), int(y)))
    # Read sequences
    for line in file:
        line = line.strip()
        if line:
            sequence = [int(num.strip()) for num in line.strip().split(',')]
            sequences.append(sequence)

total = 0

for sequence in sequences:
    page_to_index = {page: idx for idx, page in enumerate(sequence)}
    print(sequence)
    print(page_to_index)
    valid = True
    for x, y in ordering_rules:
        if x in page_to_index and y in page_to_index:
            if page_to_index[x] >= page_to_index[y]:
                valid = False
                break
    if valid:
        middle_page = get_middle_page(sequence)
        total += middle_page
print(total)


