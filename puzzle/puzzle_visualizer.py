import matplotlib.pyplot as plt
import numpy as np


def visualize_puzzle(board):

    grid = np.array(board).reshape(3, 3)

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.imshow(np.ones((3, 3)), cmap="Blues")

    for row in range(3):
        for col in range(3):

            number = grid[row, col]

            if number == 0:
                text = ""
            else:
                text = str(number)

            ax.text(
                col, row, text,
                ha="center",
                va="center",
                fontsize=28,
                fontweight="bold"
            )

    ax.set_xticks(np.arange(-0.5, 3, 1))
    ax.set_yticks(np.arange(-0.5, 3, 1))
    ax.grid(color="black", linewidth=2)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.set_title("AI 8-Puzzle Solver")

    plt.show()