
from maze.maze_logic import (
    START,
    GOAL,
    get_neighbors
)


def maze_dfs():

    stack = [START]

    visited = {START}

    parent = {START: None}

    nodes_explored = 0

    while stack:

        current = stack.pop()

        nodes_explored += 1

        if current == GOAL:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return {
                "path": path,
                "nodes_explored": nodes_explored,
                "moves": len(path) - 1
            }

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    return None
