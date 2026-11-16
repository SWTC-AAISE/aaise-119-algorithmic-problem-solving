"""Supplied readable reachability summary and small algorithm teaching tables."""

from console_style import print_color


def show_reachable(graph, order):
    """State which buildings were reached and which remain disconnected."""
    print_color("Reachable buildings: " + ", ".join(order), "success")
    not_reached = []
    for node in graph:
        if node not in order:
            not_reached.append(node)
    if not_reached:
        print("Not reachable from this start: " + ", ".join(not_reached))


def show_trace(title, trace, seen_label):
    """Print pending order and explicitly labeled membership after each processed node."""
    print_color("\nTeaching view - " + title, "heading")
    print(f"Step  Processed  {'Pending (stored order)':<30} {seen_label} (alphabetical)")
    for index, step in enumerate(trace, start=1):
        pending = ", ".join(step["pending"])
        if not pending:
            pending = "(empty)"
        seen = ", ".join(step["seen"])
        print(f"{index:<6}{step['processed']:<11}{pending:<30} {seen}")
