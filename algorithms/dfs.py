
from puzzle.puzzle_logic import (
    GOAL_STATE,
    get_neighbors
)


def dfs(start_state):

    # Create Stack
    stack = [start_state]

    # Track visited states
    visited = {start_state}

    # Store parent states
    parent = {start_state: None}

    # Count explored nodes
    nodes_explored = 0

    # Continue until Stack is empty
    while stack:

        # Remove last state (LIFO)
        current = stack.pop()

        nodes_explored += 1

        # Check goal
        if current == GOAL_STATE:

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

        # Generate neighboring states
        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    return None
