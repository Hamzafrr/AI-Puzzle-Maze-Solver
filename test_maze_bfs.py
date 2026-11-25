
from algorithms.maze_bfs import maze_bfs

result = maze_bfs()

if result:
    print("MAZE BFS SOLUTION FOUND!")

    print("Nodes Explored:", result["nodes_explored"])
    print("Total Moves:", result["moves"])

    print("\nShortest Path:")

    for step, position in enumerate(result["path"]):
        print("Step", step, ":", position)

else:
    print("No path found!")
