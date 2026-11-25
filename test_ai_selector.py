
from recommendation.ai_selector import recommend_algorithm

# Test 1: Puzzle with shortest path required
result1 = recommend_algorithm("puzzle", True)

print("TEST 1: PUZZLE")
print("Recommended Algorithm:", result1["algorithm"])
print("Reason:", result1["reason"])


# Test 2: Maze with shortest path required
result2 = recommend_algorithm("maze", True)

print("\nTEST 2: MAZE")
print("Recommended Algorithm:", result2["algorithm"])
print("Reason:", result2["reason"])


# Test 3: Maze without shortest path requirement
result3 = recommend_algorithm("maze", False)

print("\nTEST 3: MAZE WITHOUT SHORTEST PATH")
print("Recommended Algorithm:", result3["algorithm"])
print("Reason:", result3["reason"])
