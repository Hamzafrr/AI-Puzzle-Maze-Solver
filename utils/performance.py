
import time


def compare_algorithms(algorithms):

    results = []

    for name, algorithm in algorithms.items():

        start_time = time.perf_counter()

        result = algorithm()

        end_time = time.perf_counter()

        if result:

            execution_time = end_time - start_time

            results.append({
                "Algorithm": name,
                "Nodes Explored": result["nodes_explored"],
                "Total Moves": result["moves"],
                "Execution Time (seconds)": round(execution_time, 6)
            })

    return results
