
from algorithms.maze_astar import maze_astar

result = maze_astar()

if result:
    print("MAZE A* SOLUTION FOUND!")

    print("Nodes Explored:", result["nodes_explored"])
    print("Total Moves:", result["moves"])

    print("\nA* Shortest Path:")

    for step, position in enumerate(result["path"]):
        print("Step", step, ":", position)

else:
    print("No path found!")
