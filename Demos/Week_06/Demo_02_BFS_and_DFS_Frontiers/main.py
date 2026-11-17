"""Compare breadth-first and depth-first ways to inspect reachable buildings."""

from collections import deque
from graph_data import GRAPH
from graph_support import require_known_node, require_valid_references, record_step
from graph_display import show_frontier, show_reachable, show_trace
from console_style import print_color


def breadth_first(graph, start):
    """Return BFS order, teaching snapshots, and examined adjacency-entry count."""
    require_known_node(graph, start)
    require_valid_references(graph)
    queue = deque([start])
    discovered = {start}
    order = []
    trace = []
    edges_examined = 0
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            edges_examined += 1
            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)
        record_step(trace, node, queue, discovered)
    return order, trace, edges_examined


def depth_first(graph, start):
    """Return iterative DFS order, teaching snapshots, and adjacency-entry count."""
    require_known_node(graph, start)
    require_valid_references(graph)
    stack = [start]
    visited = set()
    order = []
    trace = []
    edges_examined = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph[node]):
            edges_examined += 1
            if neighbor not in visited:
                stack.append(neighbor)
        record_step(trace, node, stack, visited)
    return order, trace, edges_examined


def traverse(graph, start, strategy):
    """Keep the earlier calling interface while delegating to explicit algorithms."""
    if strategy == "BFS":
        return breadth_first(graph, start)
    if strategy == "DFS":
        return depth_first(graph, start)
    raise ValueError("strategy must be BFS or DFS")


def main():
    """Present reachable buildings first, then the small queue/stack comparison."""
    print_color("CAMPUS CONNECTION EXPLORER", "heading")
    print("Which buildings can we reach from Library?\n")
    bfs_order, bfs_trace, bfs_edges = breadth_first(GRAPH, "Library")
    dfs_order, dfs_trace, dfs_edges = depth_first(GRAPH, "Library")
    show_reachable(GRAPH, bfs_order)
    print("\nBFS visit order: " + ", ".join(bfs_order))
    print("DFS visit order: " + ", ".join(dfs_order))
    print("Visit order describes inspection, not a walking route.")

    show_trace("BFS: queue front is on the left", bfs_trace, "Discovered")
    show_trace("DFS: stack top is on the right", dfs_trace, "Processed so far")
    print("Rows show new visits; DFS skips any remaining already-processed entries.")
    show_frontier("BFS queue: FRONT -> REAR", bfs_trace, "Library",
                  "Removes the front item, then adds newly discovered neighbors at the rear.")
    show_frontier("DFS stack: BOTTOM -> TOP", dfs_trace, "Library",
                  "Removes the top item, then pushes eligible neighbors onto the top.")
    print(f"\nAdjacency entries examined: BFS {bfs_edges}; DFS {dfs_edges}.")
    print("Each of the five undirected connections has two adjacency entries.")
    print("Core traversal work is O(V + E); teaching snapshots and sorting add work.")


if __name__ == "__main__":
    main()
