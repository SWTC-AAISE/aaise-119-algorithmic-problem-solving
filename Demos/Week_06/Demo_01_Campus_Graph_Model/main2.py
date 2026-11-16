"""Documented equivalent of main.py, with the same results and algorithm behavior.

Read main.py first; use these comments to connect the code to the lecture concepts.
"""

from graph_data import GRAPH
from graph_display import show_connections, show_validation
from console_style import print_color


def validate_graph(graph, undirected=True):
    """List duplicate, unknown, or missing reciprocal neighbor references."""
    # Collect issues so the map checker can report more than one connection problem.
    errors = []
    # A dictionary key names a building; its list names directly connected buildings.
    for node, neighbors in graph.items():
        # A set keeps each neighbor once, so a shorter set reveals a duplicate entry.
        # Sets were introduced earlier; the named variable keeps this comparison visible.
        unique_neighbors = set(neighbors)
        if len(neighbors) != len(unique_neighbors):
            errors.append(f"{node}: duplicate neighbor")
        for neighbor in neighbors:
            # A connection to an undefined building is a data mistake, unlike disconnected Annex.
            if neighbor not in graph:
                errors.append(f"{node}: unknown node {neighbor}")
            # Our two-way model lists each connection from both ends.
            # Only check the reverse list after confirming that the neighbor exists.
            elif undirected and node not in graph[neighbor]:
                errors.append(f"{node}->{neighbor}: missing reciprocal connection")
    # An empty result means these connection checks found no issues, not that the model captures all reality.
    return errors


def main():
    """Show the map, check its connections, and identify one deliberate mistake."""
    print_color("CAMPUS MAP CHECK", "heading")
    print("Check direct walking connections before using this fictional map.\n")
    # Begin with the useful map information before opening the validation logic.
    show_connections(GRAPH)
    show_validation("Original map", validate_graph(GRAPH))

    # Create a separate example instead of damaging the supplied map.
    broken = {}
    for node, neighbors in GRAPH.items():
        # Copy each neighbor list as well as creating a new outer dictionary.
        # Appending Gym below must leave the original Library connections unchanged.
        # Compact equivalent: broken = {node: list(neighbors) for node, neighbors in GRAPH.items()}
        # Optional AI prompt: Explain this dictionary comprehension using the loop above, including why each list is copied.
        broken[node] = list(neighbors)
    broken["Library"].append("Gym")
    # Use the same checker for valid and deliberately broken inputs.
    show_validation("Map with a deliberately mistyped connection", validate_graph(broken))

    print("\nA cycle: Library - Atrium - Cafe - Studio - Lab - Library")
    print("Annex exists in the model but has no direct connections.")
    print("Connections work both ways; distance, hours and accessibility are not modeled.")


if __name__ == "__main__":
    main()
