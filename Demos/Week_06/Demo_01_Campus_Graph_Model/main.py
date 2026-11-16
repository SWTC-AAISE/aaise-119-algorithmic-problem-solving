"""Check whether a fictional campus map has consistent direct connections."""

from graph_data import GRAPH
from graph_display import show_connections, show_validation
from console_style import print_color


def validate_graph(graph, undirected=True):
    """List duplicate, unknown, or missing reciprocal neighbor references."""
    errors = []
    for node, neighbors in graph.items():
        unique_neighbors = set(neighbors)
        if len(neighbors) != len(unique_neighbors):
            errors.append(f"{node}: duplicate neighbor")
        for neighbor in neighbors:
            if neighbor not in graph:
                errors.append(f"{node}: unknown node {neighbor}")
            elif undirected and node not in graph[neighbor]:
                errors.append(f"{node}->{neighbor}: missing reciprocal connection")
    return errors


def main():
    """Show the map, check its connections, and identify one deliberate mistake."""
    print_color("CAMPUS MAP CHECK", "heading")
    print("Check direct walking connections before using this fictional map.\n")
    show_connections(GRAPH)
    show_validation("Original map", validate_graph(GRAPH))

    broken = {}
    for node, neighbors in GRAPH.items():
        broken[node] = list(neighbors)
    broken["Library"].append("Gym")
    show_validation("Map with a deliberately mistyped connection", validate_graph(broken))

    print("\nA cycle: Library - Atrium - Cafe - Studio - Lab - Library")
    print("Annex exists in the model but has no direct connections.")
    print("Connections work both ways; distance, hours and accessibility are not modeled.")


if __name__ == "__main__":
    main()
