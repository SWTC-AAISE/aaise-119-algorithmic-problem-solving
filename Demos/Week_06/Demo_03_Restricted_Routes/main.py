"""Find a fewest-hop campus route and avoid explicitly blocked buildings."""

from collections import deque
from graph_data import GRAPH
from route_support import validate_request, read_blocked_nodes, route_distance
from graph_display import show_route, show_parents
from console_style import print_color


def reconstruct_path(parents, goal):
    """Follow parent links back to the start, then return start-to-goal order."""
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted BFS path and parent map, or None when no path is available."""
    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)
    if start in blocked_nodes or goal in blocked_nodes:
        return None, {}
    parents = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return reconstruct_path(parents, goal), parents
        for neighbor in graph[node]:
            if neighbor not in parents and neighbor not in blocked_nodes:
                parents[neighbor] = node
                queue.append(neighbor)
    return None, parents


def main():
    """Show usable routes before the separate parent-link teaching view."""
    blocked = read_blocked_nodes()
    print_color("CAMPUS ROUTE FINDER", "heading")
    print("Find a route from Library to Studio with the fewest walking connections.")
    path, parents = shortest_hop_path(GRAPH, "Library", "Studio")
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

    show_parents(parents)
    unreachable, unused_parents = shortest_hop_path(GRAPH, "Library", "Annex")
    show_route("Library to disconnected Annex", unreachable)
    same_place, unused_parents = shortest_hop_path(GRAPH, "Library", "Library")
    show_route("Already at Library", same_place)


if __name__ == "__main__":
    main()
