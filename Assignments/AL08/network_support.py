"""Supplied model checks, defensive errors, snapshots, and Thursday input."""

import argparse
from network_data import GRAPH


def validate_model(graph):
    """List duplicate, unknown, and missing reciprocal references in this model."""
    errors = []
    for node, neighbors in graph.items():
        unique_neighbors = set(neighbors)
        if len(neighbors) != len(unique_neighbors):
            errors.append(f"{node}: duplicate neighbor")
        for neighbor in neighbors:
            if neighbor not in graph:
                errors.append(f"{node}: unknown node {neighbor}")
            elif node not in graph[neighbor]:
                errors.append(f"{node}->{neighbor}: missing reciprocal connection")
    return errors


def require_valid_model(graph):
    """Stop with a clear message when supplied connection checks find an issue."""
    errors = validate_model(graph)
    if errors:
        raise ValueError("Invalid connection model: " + "; ".join(errors))


def validate_request(graph, start, goal=None, blocked=()):
    """Keep invalid names and unknown references out of the assessed algorithms."""
    require_valid_model(graph)
    if start not in graph:
        raise ValueError(f"Unknown start: {start}")
    if goal is not None and goal not in graph:
        raise ValueError(f"Unknown goal: {goal}")
    for node in blocked:
        if node not in graph:
            raise ValueError(f"Unknown blocked node: {node}")


def record_step(trace, node, frontier, seen):
    """Save a small independent teaching snapshot after processing a new node."""
    trace.append({
        "processed": node,
        "pending": list(frontier),
        "seen": sorted(seen),
    })


def read_blocked(default_nodes):
    """Supply Thursday's optional multi-value input with the assigned default case."""
    parser = argparse.ArgumentParser(description="Workshop fewest-hop access planner")
    parser.add_argument(
        "--blocked", nargs="*", choices=list(GRAPH), default=list(default_nodes),
        help="Rooms to avoid; no option uses your assigned case; --blocked alone clears blocks.",
    )
    args = parser.parse_args()
    return args.blocked
