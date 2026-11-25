
import matplotlib.pyplot as plt
import numpy as np

from maze.maze_logic import MAZE, START, GOAL


def visualize_maze(path=None):

    grid = np.array(MAZE)

    plt.figure(figsize=(7, 7))

    plt.imshow(grid, cmap="gray_r")

    # Draw grid lines
    plt.xticks(range(len(MAZE[0])))
    plt.yticks(range(len(MAZE)))

    plt.grid(True, color="black", linewidth=2)

    # Draw solution path
    if path:
        rows = [position[0] for position in path]
        cols = [position[1] for position in path]

        plt.plot(
            cols,
            rows,
            color="blue",
            linewidth=3,
            marker="o",
            label="Solution Path"
        )

    # Starting position
    plt.scatter(
        START[1],
        START[0],
        color="green",
        s=200,
        label="Start"
    )

    # Goal position
    plt.scatter(
        GOAL[1],
        GOAL[0],
        color="red",
        s=200,
        label="Goal"
    )

    plt.title("AI Maze Solver")
    plt.legend()
    plt.gca().invert_yaxis()

    plt.show()
