def traverse(graph, start, strategy):
    """Keep the earlier calling interface while delegating to explicit algorithms."""
    if strategy == "BFS":
        return breadth_first(graph, start)
    if strategy == "DFS":
        return depth_first(graph, start)
    raise ValueError("strategy must be BFS or DFS")