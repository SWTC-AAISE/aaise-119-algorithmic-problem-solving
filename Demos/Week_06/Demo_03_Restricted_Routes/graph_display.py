"""Readable route results and a separately labeled parent-link teaching view."""

from console_style import print_color
from route_support import route_distance


def show_route(label, path):
    """Show a route and hop count or a clear no-route message."""
    print_color("\n" + label, "heading")
    if path is None:
        print_color("No permitted route is available.", "caution")
        return
    print_color("Route: " + " -> ".join(path), "success")
    print(f"Walking connections: {len(path) - 1}")
    print(f"Illustrative distance: {route_distance(path)} units")


def show_parents(parents):
    """Explain each BFS discovery link without displaying a raw dictionary."""
    print_color("\nTeaching view - how BFS first reached each building", "heading")
    for node, parent in parents.items():
        if parent is None:
            print(f"  {node}: start building")
        else:
            print(f"  {node}: first reached from {parent}")
