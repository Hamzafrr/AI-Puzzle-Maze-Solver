from algorithms.dfs import dfs

start_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

result = dfs(start_state)

if result:
    print("DFS SOLUTION FOUND!")
    print("Nodes Explored:", result["nodes_explored"])
    print("Total Moves:", result["moves"])

    print("\nFirst 3 Steps:")
    for step, state in enumerate(result["path"][:3]):
        print("\nStep:", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])

    print("\nLast 3 Steps:")
    start = max(0, len(result["path"]) - 3)

    for step, state in enumerate(result["path"][-3:], start=start):
        print("\nStep:", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
else:
    print("No solution found!")