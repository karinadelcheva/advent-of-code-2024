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

