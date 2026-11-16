"""Documented equivalent of main.py, with the same results and algorithm behavior.

Read main.py first; use these comments to connect the code to the lecture concepts.
"""

from collections import deque
from graph_data import GRAPH
from graph_support import require_known_node, require_valid_references, record_step
from graph_display import show_reachable, show_trace
from console_style import print_color


def breadth_first(graph, start):
    """Return BFS order, teaching snapshots, and examined adjacency-entry count."""
    require_known_node(graph, start)
    # Supplied quality checks prevent unclear failures; the traversal lesson starts below.
    require_valid_references(graph)
    # The queue holds discovered buildings waiting for inspection, with the next at the left.
    queue = deque([start])
    # For BFS, mark on enqueue so a building enters the queue only once.
    discovered = {start}
    order = []
    trace = []
    edges_examined = 0
    while queue:
        # FIFO takes the oldest waiting building, producing outward layers.
        node = queue.popleft()
        # Processed order differs from membership in the discovered set.
        order.append(node)
        for neighbor in graph[node]:
            edges_examined += 1
            # A cycle may lead back to a known building, so do not schedule it again.
            if neighbor not in discovered:
                discovered.add(neighbor)
                # Newly discovered buildings wait behind the ones already in the queue.
                queue.append(neighbor)
        # This supplied helper saves a teaching snapshot after processing the node.
        # Snapshot copies and sorted labels add work beyond the core traversal.
        record_step(trace, node, queue, discovered)
    return order, trace, edges_examined


def depth_first(graph, start):
    """Return iterative DFS order, teaching snapshots, and adjacency-entry count."""
    require_known_node(graph, start)
    require_valid_references(graph)
    # The right end of this familiar list is the top of our LIFO stack.
    stack = [start]
    # For this DFS, visited means actually taken from the stack and processed.
    visited = set()
    order = []
    trace = []
    edges_examined = 0
    while stack:
        # The last neighbor pushed becomes the next branch we follow.
        node = stack.pop()
        # A building can be waiting more than once; skip an entry already processed.
        # This small guard keeps cycles from causing repeated processing.
        if node in visited:
            continue
        # Mark here, when processing begins, instead of reserving every sibling in advance.
        visited.add(node)
        order.append(node)
        # Push in reverse list order so the first listed neighbor is taken next.
        # This changes stack order without reversing the original graph lists.
        for neighbor in reversed(graph[node]):
            edges_examined += 1
            if neighbor not in visited:
                stack.append(neighbor)
        # The snapshot shows the stored stack order, with its top on the right.
        record_step(trace, node, stack, visited)
    return order, trace, edges_examined


def traverse(graph, start, strategy):
    """Keep the earlier calling interface while delegating to explicit algorithms."""
    # This compatibility wrapper preserves the earlier API; read the two explicit algorithms first.
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
    # Give the user the reachability answer before the separate teaching tables.
    show_reachable(GRAPH, bfs_order)
    print("\nBFS visit order: " + ", ".join(bfs_order))
    print("DFS visit order: " + ", ".join(dfs_order))
    print("Visit order describes inspection, not a walking route.")

    # BFS labels discovered membership; DFS labels processed membership.
    # Alphabetical set labels help reading but are not a second visit order.
    show_trace("BFS: queue front is on the left", bfs_trace, "Discovered")
    show_trace("DFS: stack top is on the right", dfs_trace, "Processed so far")
    print("Rows show new visits; DFS skips any remaining already-processed entries.")
    print(f"\nAdjacency entries examined: BFS {bfs_edges}; DFS {dfs_edges}.")
    print("Each of the five undirected connections has two adjacency entries.")
    print("Core traversal work is O(V + E); teaching snapshots and sorting add work.")


if __name__ == "__main__":
    main()
