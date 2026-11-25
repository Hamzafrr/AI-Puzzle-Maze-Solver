
from algorithms.maze_dfs import maze_dfs

result = maze_dfs()

if result:
    print("MAZE DFS SOLUTION FOUND!")

    print("Nodes Explored:", result["nodes_explored"])
    print("Total Moves:", result["moves"])

    print("\nDFS Path:")

    for step, position in enumerate(result["path"]):
        print("Step", step, ":", position)

else:
    print("No path found!")
