"""Readable map and validation messages, separate from graph checks."""

from console_style import print_color


def show_connections(graph):
    """List each building's direct connections in ordinary readable text."""
    print_color("Direct walking connections", "heading")
    for node, neighbors in graph.items():
        if neighbors:
            print(f"  {node}: {', '.join(neighbors)}")
        else:
            print(f"  {node}: No direct connections in this model")


def show_validation(label, errors):
    """Report either a clear success message or the individual connection issues."""
    print_color("\n" + label, "heading")
    if not errors:
        print_color("  Connection checks passed.", "success")
    else:
        print_color("  Please correct these connections:", "caution")
        for error in errors:
            print("  - " + error)
