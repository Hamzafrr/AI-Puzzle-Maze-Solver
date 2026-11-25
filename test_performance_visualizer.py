from algorithms.maze_bfs import maze_bfs
from algorithms.maze_dfs import maze_dfs
from algorithms.maze_astar import maze_astar

from utils.performance import compare_algorithms
from utils.performance_visualizer import plot_performance


algorithms = {
    "BFS": maze_bfs,
    "DFS": maze_dfs,
    "A*": maze_astar
}

results = compare_algorithms(algorithms)

print("Displaying Performance Graphs...")

plot_performance(results)