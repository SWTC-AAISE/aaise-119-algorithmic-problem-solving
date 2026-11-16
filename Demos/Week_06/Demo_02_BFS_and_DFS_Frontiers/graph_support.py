"""Supplied quality checks and small teaching snapshots, separate from traversal."""


def require_known_node(graph, node):
    """Reject a requested building that is absent from the model."""
    if node not in graph:
        raise ValueError(f"Unknown building: {node}")


def require_valid_references(graph):
    """Report an unknown neighbor clearly instead of exposing a dictionary KeyError."""
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError(f"{node} refers to unknown building: {neighbor}")


def record_step(trace, node, frontier, seen):
    """Save independent pending/seen snapshots for this small teaching example."""
    trace.append({
        "processed": node,
        "pending": list(frontier),
        "seen": sorted(seen),
    })
