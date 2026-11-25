import matplotlib.pyplot as plt


def plot_performance(results):

    names = [item["Algorithm"] for item in results]
    nodes = [item["Nodes Explored"] for item in results]
    times = [item["Execution Time (seconds)"] for item in results]

    # Chart 1: Nodes Explored
    plt.figure(figsize=(8, 5))
    plt.bar(names, nodes)
    plt.title("Nodes Explored Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes Explored")
    plt.show()

    # Chart 2: Execution Time
    plt.figure(figsize=(8, 5))
    plt.bar(names, times)
    plt.title("Execution Time Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Execution Time (seconds)")
    plt.show()