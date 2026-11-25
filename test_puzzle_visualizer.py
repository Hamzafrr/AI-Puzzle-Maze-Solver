from puzzle.puzzle_visualizer import visualize_puzzle

start_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

print("Displaying 8-Puzzle Board...")

visualize_puzzle(start_state)