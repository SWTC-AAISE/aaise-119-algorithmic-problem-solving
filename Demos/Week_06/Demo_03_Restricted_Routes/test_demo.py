"""Instructor checks for fewest-hop routes and clear defensive error handling."""

from copy import deepcopy
from main import GRAPH, route_distance, shortest_hop_path, reconstruct_path


def expect_value_error(function, *args):
    """Require a clear invalid-input exception instead of an unhandled KeyError."""
    try:
        function(*args)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


def self_check():
    """Check normal routes, restrictions, reconstruction, boundaries, and ownership."""
    original = deepcopy(GRAPH)
    path, parents = shortest_hop_path(GRAPH, "Library", "Studio")
    assert path == ["Library", "Lab", "Studio"]
    assert route_distance(path) == 16
    assert parents["Library"] is None
    assert reconstruct_path(parents, "Studio") == path
    restricted, restricted_parents = shortest_hop_path(GRAPH, "Library", "Studio", ["Lab"])
    assert restricted == ["Library", "Atrium", "Cafe", "Studio"]
    assert route_distance(restricted) == 3
    for index in range(1, len(restricted)):
        assert restricted[index] in GRAPH[restricted[index - 1]]
    assert "Lab" not in restricted_parents
    assert shortest_hop_path(GRAPH, "Library", "Annex")[0] is None
    assert shortest_hop_path(GRAPH, "Library", "Library")[0] == ["Library"]
    assert shortest_hop_path(GRAPH, "Library", "Studio", ["Studio"]) == (None, {})
    assert shortest_hop_path(GRAPH, "Library", "Studio", ["Library"]) == (None, {})
    assert shortest_hop_path(GRAPH, "Library", "Studio", ["Lab", "Cafe"])[0] is None
    assert shortest_hop_path(GRAPH, "Library", "Studio", [])[0] == path
    assert shortest_hop_path({"A": ["A"]}, "A", "A")[0] == ["A"]
    expect_value_error(shortest_hop_path, GRAPH, "Missing", "Studio")
    expect_value_error(shortest_hop_path, GRAPH, "Library", "Missing")
    expect_value_error(shortest_hop_path, GRAPH, "Library", "Studio", ["Missing"])
    expect_value_error(shortest_hop_path, {"A": ["Missing"], "B": []}, "A", "B")
    expect_value_error(route_distance, ["Library", "Annex"])
    assert GRAPH == original


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
