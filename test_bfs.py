
from algorithms.bfs import bfs

start_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

result = bfs(start_state)

if result:

    print("BFS SOLUTION FOUND!")

    print("Nodes Explored:", result["nodes_explored"])

    print("Total Moves:", result["moves"])

    print("\nSolution Steps:")

    for step, state in enumerate(result["path"]):

        print("\nStep:", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])

else:
    print("No solution found!")
