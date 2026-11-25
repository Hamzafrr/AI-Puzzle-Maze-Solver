
from utils.performance import compare_algorithms

from algorithms.maze_bfs import maze_bfs
from algorithms.maze_dfs import maze_dfs
from algorithms.maze_astar import maze_astar


algorithms = {
    "BFS": maze_bfs,
    "DFS": maze_dfs,
    "A*": maze_astar
}

results = compare_algorithms(algorithms)

print("MAZE ALGORITHM PERFORMANCE COMPARISON")
print("-------------------------------------")

for result in results:

    print("\nAlgorithm:", result["Algorithm"])
    print("Nodes Explored:", result["Nodes Explored"])
    print("Total Moves:", result["Total Moves"])
    print("Execution Time:", result["Execution Time (seconds)"], "seconds")
