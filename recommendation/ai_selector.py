
def recommend_algorithm(problem_type, shortest_path=True):

    if problem_type == "puzzle":

        if shortest_path:
            return {
                "algorithm": "A* Search",
                "reason": "A* uses Manhattan Distance to guide the search and finds an optimal solution."
            }

        else:
            return {
                "algorithm": "DFS",
                "reason": "DFS explores deeply and can find a solution without guaranteeing the shortest path."
            }

    elif problem_type == "maze":

        if shortest_path:
            return {
                "algorithm": "A* Search",
                "reason": "A* uses Manhattan Distance to guide the search toward the goal."
            }

        else:
            return {
                "algorithm": "DFS",
                "reason": "DFS explores one route deeply before trying another."
            }

    else:
        return {
            "algorithm": "BFS",
            "reason": "BFS is a general search method for finding the shortest path in an unweighted problem."
        }
