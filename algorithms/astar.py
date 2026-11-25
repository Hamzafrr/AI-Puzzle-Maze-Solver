
import heapq

from puzzle.puzzle_logic import (
    GOAL_STATE,
    get_neighbors
)


def manhattan_distance(board):
    distance = 0

    for index, tile in enumerate(board):

        if tile == 0:
            continue

        current_row = index // 3
        current_col = index % 3

        goal_index = GOAL_STATE.index(tile)

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def astar(start_state):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (manhattan_distance(start_state), 0, start_state)
    )

    visited = set()
    parent = {start_state: None}
    g_score = {start_state: 0}

    nodes_explored = 0

    while priority_queue:

        f_score, current_cost, current = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

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
