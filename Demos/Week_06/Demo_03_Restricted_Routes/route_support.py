"""Supplied route input, quality checks and illustrative distance information."""

import argparse
from graph_data import GRAPH
from graph_support import require_known_node, require_valid_references

# Distances are fictional comparison units, not a weighted pathfinding algorithm.
DISTANCES = {
    "Library": {"Atrium": 1, "Lab": 8},
    "Atrium": {"Library": 1, "Cafe": 1},
    "Cafe": {"Atrium": 1, "Studio": 1},
    "Lab": {"Library": 8, "Studio": 8},
    "Studio": {"Lab": 8, "Cafe": 1},
    "Annex": {},
}


def validate_request(graph, start, goal, blocked):
    """Reject unknown names/references with a clear error before searching."""
    require_known_node(graph, start)
    require_known_node(graph, goal)
    for node in blocked:
        require_known_node(graph, node)
    require_valid_references(graph)


def route_distance(path):
    """Add supplied distance units for adjacent pairs in an existing campus route."""
    if path is None:
        raise ValueError("A route is needed before adding its distance.")
    total = 0
    for index in range(1, len(path)):
        previous = path[index - 1]
        current = path[index]
        if previous not in DISTANCES or current not in DISTANCES[previous]:
            raise ValueError(f"No distance is supplied for {previous} to {current}.")
        total += DISTANCES[previous][current]
    return total


def read_blocked_nodes():
    """Supply the bounded multi-value option introduced in Thursday's lesson."""
    parser = argparse.ArgumentParser(description="Find a fewest-hop campus route.")
    parser.add_argument(
        "--blocked", nargs="*", choices=list(GRAPH), default=["Lab"],
        help="Buildings to avoid (default: Lab); --blocked alone means no blocks.",
    )
    args = parser.parse_args()
    return args.blocked
