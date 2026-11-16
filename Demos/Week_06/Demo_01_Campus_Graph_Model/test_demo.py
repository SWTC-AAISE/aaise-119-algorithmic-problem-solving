"""Regression checks, separate from the classroom application."""

from main import (
    GRAPH,
    validate_graph,
)


def self_check():
    """Check duplicate, unknown, reciprocal, directed, and empty-model behavior."""
    assert validate_graph(GRAPH) == []
    assert validate_graph({"A": ["missing"]}) == ["A: unknown node missing"]
    assert validate_graph({"A": ["B"], "B": []})
    assert validate_graph({"A": ["B"], "B": []}, undirected=False) == []
    assert validate_graph({}) == []
    assert validate_graph({"A": ["A", "A"]}) == ["A: duplicate neighbor"]


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
