
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Puzzle algorithms
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar

# Maze algorithms
from algorithms.maze_bfs import maze_bfs
from algorithms.maze_dfs import maze_dfs
from algorithms.maze_astar import maze_astar

# Maze settings
from maze.maze_logic import MAZE, START, GOAL

# Performance analysis
from utils.performance import compare_algorithms

# AI recommendation
from recommendation.ai_selector import recommend_algorithm


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Puzzle & Maze Solver",
    page_icon="🧩",
    layout="wide"
)

st.title("🧩 AI Puzzle & Maze Solver")
st.subheader("DSA Lab Final Project ")

st.write(
    "An AI-based application that solves 8-Puzzle "
    "and Maze problems using BFS, DFS and A* algorithms."
)

st.divider()


# ==========================================
# SIDEBAR SETTINGS
# ==========================================

st.sidebar.title("⚙️ Solver Settings")

problem_type = st.sidebar.selectbox(
    "Select Problem",
    ["8-Puzzle", "Maze"]
)

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["BFS", "DFS", "A*"]
)

shortest_path = st.sidebar.checkbox(
    "Prioritize shortest path",
    value=True
)


# ==========================================
# PROBLEM SELECTION
# ==========================================

st.header("Problem Selection")

if problem_type == "8-Puzzle":
    st.info("You selected the 8-Puzzle Solver.")
    st.write("Solve a 3×3 sliding number puzzle.")

else:
    st.info("You selected the Maze Solver.")
    st.write("Find a path from Start to Goal.")

st.divider()


# ==========================================
# ALGORITHM SELECTION
# ==========================================

st.header("Algorithm Selection")
st.write(f"Selected Algorithm: **{algorithm}**")

st.divider()


# ==========================================
# SOLUTION SECTION
# ==========================================

st.header("Solution")


# ==========================================
# 8-PUZZLE SOLVER
# ==========================================

if problem_type == "8-Puzzle":

    st.subheader("Enter Starting Puzzle")

    start_state = st.text_input(
        "Enter 9 numbers separated by commas",
        "1,2,3,4,0,6,7,5,8"
    )

    if st.button("Solve Puzzle"):

        try:
            numbers = tuple(
                int(x.strip()) for x in start_state.split(",")
            )

            if len(numbers) != 9 or set(numbers) != set(range(9)):

                st.error("Enter numbers 0 to 8 exactly once.")

            else:

                algorithm_functions = {
                    "BFS": bfs,
                    "DFS": dfs,
                    "A*": astar
                }

                with st.spinner(f"Running {algorithm}..."):
                    result = algorithm_functions[algorithm](numbers)

                if result:

                    st.success("Puzzle solved successfully!")

                    col1, col2 = st.columns(2)

                    col1.metric(
                        "Nodes Explored",
                        result["nodes_explored"]
                    )

                    col2.metric(
                        "Total Moves",
                        result["moves"]
                    )

                    with st.expander("View Solution Steps"):

                        path = result["path"]

                        if len(path) <= 30:
                            steps = list(enumerate(path))
                        else:
                            steps = (
                                list(enumerate(path[:10])) +
                                list(enumerate(
                                    path[-5:],
                                    start=len(path) - 5
                                ))
                            )

                        for step, board in steps:

                            st.write(f"Step {step}:")

                            st.code(
                                f"{board[0:3]}\n"
                                f"{board[3:6]}\n"
                                f"{board[6:9]}"
                            )

                        if len(path) > 30:
                            st.info("Middle steps are hidden.")

                else:
                    st.error("No solution found!")

        except ValueError:
            st.error("Please enter valid numbers separated by commas.")


# ==========================================
# MAZE SOLVER
# ==========================================

elif problem_type == "Maze":

    st.subheader("Maze Visualization")

    st.write(
        "Green = Start | Red = Goal | "
        "White = Open Path | Black = Wall"
    )

    def draw_maze(path=None):

        grid = np.array(MAZE)

        fig, ax = plt.subplots(figsize=(6, 6))

        ax.imshow(grid, cmap="gray_r")

        ax.set_xticks(range(len(MAZE[0])))
        ax.set_yticks(range(len(MAZE)))

        ax.grid(True, color="black", linewidth=2)

        if path:

            rows = [position[0] for position in path]
            cols = [position[1] for position in path]

            ax.plot(
                cols,
                rows,
                color="blue",
                linewidth=3,
                marker="o",
                label="Solution Path"
            )

        ax.scatter(
            START[1], START[0],
            color="green", s=200, label="Start"
        )

        ax.scatter(
            GOAL[1], GOAL[0],
            color="red", s=200, label="Goal"
        )

        ax.set_title("AI Maze Solver")
        ax.legend()
        ax.invert_yaxis()

        return fig

    st.pyplot(draw_maze())

    if st.button("Solve Maze"):

        maze_algorithms = {
            "BFS": maze_bfs,
            "DFS": maze_dfs,
            "A*": maze_astar
        }

        with st.spinner(f"Running {algorithm}..."):
            result = maze_algorithms[algorithm]()

        if result:

            st.success("Maze solved successfully!")

            col1, col2 = st.columns(2)

            col1.metric(
                "Nodes Explored",
                result["nodes_explored"]
            )

            col2.metric(
                "Total Moves",
                result["moves"]
            )

            st.subheader("Solution Path")

            st.pyplot(draw_maze(result["path"]))

            with st.expander("View Path Coordinates"):

                for step, position in enumerate(result["path"]):
                    st.write(f"Step {step}: {position}")

        else:
            st.error("No path found!")


# ==========================================
# PERFORMANCE ANALYSIS
# ==========================================

st.divider()
st.header("📊 Performance Analysis")

st.write(
    "Compare BFS, DFS and A* based on nodes explored, "
    "total moves and execution time."
)

if problem_type == "Maze":

    performance_algorithms = {
        "BFS": maze_bfs,
        "DFS": maze_dfs,
        "A*": maze_astar
    }

else:

    try:
        performance_state = tuple(
            int(x.strip()) for x in start_state.split(",")
        )

        if (
            len(performance_state) != 9
            or set(performance_state) != set(range(9))
        ):
            performance_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    except ValueError:
        performance_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    performance_algorithms = {
        "BFS": lambda: bfs(performance_state),
        "DFS": lambda: dfs(performance_state),
        "A*": lambda: astar(performance_state)
    }


if st.button("Run Performance Comparison"):

    with st.spinner("Comparing all three algorithms..."):

        performance_results = compare_algorithms(
            performance_algorithms
        )

    if performance_results:

        st.success("Performance comparison completed!")

        performance_df = pd.DataFrame(performance_results)

        st.subheader("Performance Results")

        st.dataframe(
            performance_df,
            use_container_width=True,
            hide_index=True
        )

        chart_data = performance_df.set_index("Algorithm")

        st.subheader("Nodes Explored Comparison")

        st.bar_chart(chart_data[["Nodes Explored"]])

        st.subheader("Total Moves Comparison")

        st.bar_chart(chart_data[["Total Moves"]])

        st.subheader("Execution Time Comparison")

        st.bar_chart(
            chart_data[["Execution Time (seconds)"]]
        )

        st.caption(
            "Execution time can vary between different runs."
        )

    else:
        st.error("Performance comparison could not be completed.")


# ==========================================
# AI RECOMMENDATION
# ==========================================

st.divider()
st.header("🤖 AI Recommendation")

problem_key = (
    "puzzle" if problem_type == "8-Puzzle" else "maze"
)

recommendation = recommend_algorithm(
    problem_key,
    shortest_path=shortest_path
)

st.success(
    f"Recommended Algorithm: {recommendation['algorithm']}"
)

st.write("**Reason:**")
st.write(recommendation["reason"])

st.caption(
    "This recommendation uses a rule-based selection system."
)
