
# 0 = Open path
# 1 = Wall

MAZE = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Starting position
START = (0, 0)

# Goal position
GOAL = (4, 4)


def is_valid_position(row, col):
    rows = len(MAZE)
    cols = len(MAZE[0])

    if row < 0 or row >= rows:
        return False

    if col < 0 or col >= cols:
        return False

    if MAZE[row][col] == 1:
        return False

    return True


def get_neighbors(position):
    row, col = position

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if is_valid_position(new_row, new_col):
            neighbors.append((new_row, new_col))

    return neighbors
