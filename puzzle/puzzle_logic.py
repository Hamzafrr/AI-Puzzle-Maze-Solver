
# Goal state
GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Display puzzle board
def display_board(board):

    for i in range(0, 9, 3):
        print(board[i:i+3])


# Find empty space
def find_blank(board):

    return board.index(0)


# Generate valid movements
def get_neighbors(board):

    blank = find_blank(board)

    neighbors = []

    row = blank // 3
    col = blank % 3

    # Possible movements
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_board = list(board)

            new_board[blank], new_board[new_blank] = (
                new_board[new_blank],
                new_board[blank]
            )

            neighbors.append(tuple(new_board))

    return neighbors
