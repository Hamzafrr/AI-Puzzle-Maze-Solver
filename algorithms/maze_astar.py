
import heapq

from maze.maze_logic import (
    START,
    GOAL,
    get_neighbors
)


def manhattan_distance(position):

    row, col = position

    goal_row, goal_col = GOAL

    return abs(row - goal_row) + abs(col - goal_col)


def maze_astar():

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (manhattan_distance(START), 0, START)
    )

    visited = set()

    parent = {START: None}

    g_score = {START: 0}

    nodes_explored = 0

    while priority_queue:

        f_score, current_cost, current = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)

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

            new_cost = current_cost + 1

            if new_cost < g_score.get(neighbor, float("inf")):

                g_score[neighbor] = new_cost

                parent[neighbor] = current

                new_f_score = (
                    new_cost + manhattan_distance(neighbor)
                )

                heapq.heappush(
                    priority_queue,
                    (new_f_score, new_cost, neighbor)
                )

    return None
