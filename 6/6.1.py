def main():
    # Read the map from 'input.txt'
    with open('input.txt', 'r') as file:
        raw_map = [list(line.rstrip('\n')) for line in file]

    num_rows = len(raw_map)
    num_cols = max(len(row) for row in raw_map)

    # Normalize the map: make all rows the same length
    for row in raw_map:
        if len(row) < num_cols:
            row.extend([' '] * (num_cols - len(row)))  # Fill with spaces for missing positions

    # Directions: Up, Right, Down, Left
    directions = ['^', '>', 'v', '<']
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find the guard's starting position and direction
    for r in range(num_rows):
        for c in range(num_cols):
            cell = raw_map[r][c]
            if cell in directions:
                current_r, current_c = r, c
                facing_index = directions.index(cell)
                break
        else:
            continue
        break
    else:
        print("Guard's starting position not found.")
        return

    visited_positions = set()
    visited_positions.add((current_r, current_c))

    while True:
        dr, dc = deltas[facing_index]
        next_r = current_r + dr
        next_c = current_c + dc

        # Check if next position is outside the map boundaries
        if not (0 <= next_r < num_rows and 0 <= next_c < num_cols):
            break  # Guard leaves the map

        # Get the content of the next cell
        next_cell = raw_map[next_r][next_c]

        # If there's an obstacle or space (unmapped area), turn right
        if next_cell == '#' or next_cell == ' ':
            facing_index = (facing_index + 1) % 4  # Turn right 90 degrees
        else:
            # Move forward
            current_r, current_c = next_r, next_c
            visited_positions.add((current_r, current_c))

    print(len(visited_positions))


main()
