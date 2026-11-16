"""Supplied staged presentation, keeping UI and parser work out of the algorithms."""

from network_data import GRAPH, START, GOAL, RESTRICTIONS
from network_support import validate_model, read_blocked
from network_display import show_model, show_model_result, show_traversal, show_route, show_list
from console_style import print_color


def run(stage, breadth_first, depth_first, shortest_hop_path, personal_case):
    """Present only the current week's completed stages using supplied local data."""
    if stage not in (1, 2, 3):
        raise ValueError("STAGE must be 1, 2, or 3")
    blocked = None
    if stage == 3:
        if personal_case not in RESTRICTIONS:
            raise ValueError("Choose your issued restriction case A, B, or C")
        blocked = read_blocked(RESTRICTIONS[personal_case]["blocked"])
    show_model(GRAPH)
    errors = validate_model(GRAPH)
    show_model_result(errors)
    if errors or stage == 1:
        return
    bfs_order, bfs_trace, bfs_edges = breadth_first(GRAPH, START)
    dfs_order, dfs_trace, dfs_edges = depth_first(GRAPH, START)
    print_color("\nReachability from " + START, "heading")
    show_list("Reached rooms: ", bfs_order)
    not_reached = []
    for node in GRAPH:
        if node not in bfs_order:
            not_reached.append(node)
    if not_reached:
        show_list("Not reached: ", not_reached)
    show_traversal("BFS - queue front left", bfs_order, bfs_trace, bfs_edges, "Discovered")
    show_traversal("DFS - stack top right", dfs_order, dfs_trace, dfs_edges, "Processed so far")
    print("Pending DFS entries already processed are skipped; visit order is not a walking route.")
    print("Core traversal is O(V + E); teaching snapshots and sorting add work.")
    if stage == 3:
        baseline, baseline_parents = shortest_hop_path(GRAPH, START, GOAL)
        show_route("All rooms available: Entrance to Loading", baseline)
        print_color("\nPersonal restriction case " + personal_case, "heading")
        if blocked:
            print("Rooms to avoid: " + ", ".join(blocked))
        else:
            print("No rooms blocked in this command-line run.")
        restricted, restricted_parents = shortest_hop_path(GRAPH, START, GOAL, blocked)
        show_route("Route under the selected restriction", restricted)
        print("Fewest hops under this model; distance and travel time are not represented.")
