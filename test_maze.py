
from maze.maze_logic import (
    MAZE,
    START,
    GOAL,
    is_valid_position,
    get_neighbors
)

print("MAZE:")
for row in MAZE:
    print(row)

print("\nStarting Position:", START)
print("Goal Position:", GOAL)

print("\nValid Neighbors of Start:")
print(get_neighbors(START))

print("\nPosition Tests:")
print("(0, 1):", is_valid_position(0, 1))
print("(0, 2):", is_valid_position(0, 2))
print("(5, 5):", is_valid_position(5, 5))
