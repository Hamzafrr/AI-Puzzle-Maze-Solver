
from algorithms.maze_bfs import maze_bfs
from maze.maze_visualizer import visualize_maze

# Find the shortest path using BFS
result = maze_bfs()

if result:
    print("Displaying Maze Solution...")
    visualize_maze(result["path"])
else:
    print("No path found!")
