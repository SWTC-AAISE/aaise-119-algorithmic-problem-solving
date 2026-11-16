"""Documented equivalent of main.py, with the same results and algorithm behavior.

Read main.py first; use these comments to connect the code to the lecture concepts.
"""

from collections import deque
from graph_data import GRAPH
from route_support import validate_request, read_blocked_nodes, route_distance
from graph_display import show_route, show_parents
from console_style import print_color


def reconstruct_path(parents, goal):
    """Follow parent links back to the start, then return start-to-goal order."""
    path = []
    # Each parent tells us which earlier building first led to this one.
    node = goal
    # For Studio, the baseline chain is Studio, Lab, Library, then None.
    # None marks the start boundary rather than another building.
    while node is not None:
        path.append(node)
        # Move backward one parent link; this helper receives the map created by BFS.
        node = parents[node]
    # Reverse our new result list so the user receives Library, Lab, Studio.
    path.reverse()
    return path


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted BFS path and parent map, or None when no path is available."""
    # A set supports simple membership checks; blocks name buildings, not edges.
    blocked_nodes = set(blocked)
    # Supplied quality error handling reports unknown references clearly before searching.
    validate_request(graph, start, goal, blocked_nodes)
    # A blocked endpoint means no permitted route under this policy.
    if start in blocked_nodes or goal in blocked_nodes:
        return None, {}
    # The parent map also records which buildings BFS has already discovered.
    # The start has no earlier building, so its parent is None.
    parents = {start: None}
    # BFS schedules outward layers using the queue, preserving the fewest-hop objective.
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # Once BFS processes the goal, follow its saved parent chain.
        # If start equals goal, that chain contains only the start, giving zero hops.
        if node == goal:
            return reconstruct_path(parents, goal), parents
        for neighbor in graph[node]:
            # Only undiscovered, permitted neighbors enter the queue.
            if neighbor not in parents and neighbor not in blocked_nodes:
                # Save the first predecessor before enqueueing; this is the route evidence.
                parents[neighbor] = node
                queue.append(neighbor)
    # An exhausted queue means this search found no permitted route to the goal.
    return None, parents


def main():
    """Show usable routes before the separate parent-link teaching view."""
    # The supplied parser extends Week 5 input handling, not pathfinding itself.
    # No option blocks Lab; --blocked alone blocks none; --blocked Lab Cafe supplies two names.
    blocked = read_blocked_nodes()
    print_color("CAMPUS ROUTE FINDER", "heading")
    print("Find a route from Library to Studio with the fewest walking connections.")
    path, parents = shortest_hop_path(GRAPH, "Library", "Studio")
    # Start with the useful route and hop count before showing any parent state.
    show_route("With all buildings available", path)

    print_color("\nBuildings to avoid", "heading")
    if blocked:
        print(", ".join(blocked))
    else:
        print("None - all buildings remain available.")
    restricted, restricted_parents = shortest_hop_path(GRAPH, "Library", "Studio", blocked)
    show_route("With the selected restrictions", restricted)
    print("\nFewest hops does not guarantee the shortest distance or travel time.")
    print("Distances are supplied illustrative units; BFS does not optimize them.")

    # This separate teaching view explains the first discovery links.
    # The distance helper is supplied illustration; BFS still chooses by hops alone.
    show_parents(parents)
    # Annex is a valid model entry with no connecting path, not malformed input.
    unreachable, unused_parents = shortest_hop_path(GRAPH, "Library", "Annex")
    show_route("Library to disconnected Annex", unreachable)
    same_place, unused_parents = shortest_hop_path(GRAPH, "Library", "Library")
    show_route("Already at Library", same_place)


if __name__ == "__main__":
    main()
