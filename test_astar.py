
from algorithms.astar import astar

start_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

result = astar(start_state)

if result:
    print("A* SOLUTION FOUND!")
    print("Nodes Explored:", result["nodes_explored"])
    print("Total Moves:", result["moves"])

    print("\nSolution Path:")

    for step, state in enumerate(result["path"]):
        print("\nStep:", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])

else:
    print("No solution found!")
