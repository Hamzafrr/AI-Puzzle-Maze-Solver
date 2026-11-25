from puzzle.puzzle_logic import *

board = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

print("Original Puzzle:")
display_board(board)

print("\nBlank Position:")
print(find_blank(board))

print("\nPossible Next States:")

for state in get_neighbors(board):
    display_board(state)
    print()