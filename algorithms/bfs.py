
from collections import deque

from puzzle.puzzle_logic import (
    GOAL_STATE,
    get_neighbors
)


def bfs(start_state):

    # Create Queue
    queue = deque([start_state])

    # Track visited states
    visited = {start_state}

    # Store parent of each state
    parent = {start_state: None}

    # Count explored nodes
    nodes_explored = 0

    # Continue until Queue is empty
    while queue:

        # Remove first state from Queue
        current = queue.popleft()

        nodes_explored += 1

        # Check if goal is reached
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

                queue.append(neighbor)

    return None
