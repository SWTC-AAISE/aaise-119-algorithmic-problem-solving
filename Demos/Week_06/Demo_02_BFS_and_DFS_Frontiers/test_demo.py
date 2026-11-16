"""Instructor checks for traversal behavior; unusual cases are not another lesson."""

from copy import deepcopy
from main import GRAPH, breadth_first, depth_first, traverse


def expect_value_error(function, *args):
    """Require a useful input error instead of a raw dictionary failure."""
    try:
        function(*args)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


def self_check():
    """Check normal orders, cycle handling, actual depth-first behavior, and errors."""
    original = deepcopy(GRAPH)
    bfs, trace, edges = breadth_first(GRAPH, "Library")
    dfs, dfs_trace, dfs_edges = depth_first(GRAPH, "Library")
    assert bfs == ["Library", "Atrium", "Lab", "Cafe", "Studio"]
    assert dfs == ["Library", "Atrium", "Cafe", "Studio", "Lab"]
    assert edges == dfs_edges == 10
    assert len(bfs) == len(set(bfs))
    assert len(dfs) == len(set(dfs))
    assert set(bfs) == set(dfs) == set(GRAPH) - {"Annex"}
    assert trace[0]["pending"] == ["Atrium", "Lab"]
    assert trace[0]["seen"] == ["Atrium", "Lab", "Library"]
    assert dfs_trace[0]["seen"] == ["Library"]
    assert traverse(GRAPH, "Library", "BFS")[0] == bfs
    assert traverse(GRAPH, "Library", "DFS")[0] == dfs
    # A connection from a deeper branch must remain available even if also pending.
    cross_connected = {
        "A": ["B", "C"], "B": ["A", "D", "E"],
        "C": ["A", "D"], "D": ["B", "C"], "E": ["B"],
    }
    assert depth_first(cross_connected, "A")[0] == ["A", "B", "D", "C", "E"]
    for function in [breadth_first, depth_first]:
        assert function(GRAPH, "Annex")[0] == ["Annex"]
        assert function({"A": ["A"]}, "A")[0] == ["A"]
        expect_value_error(function, GRAPH, "Missing")
        expect_value_error(function, {"A": ["Missing"]}, "A")
    expect_value_error(traverse, GRAPH, "Library", "OTHER")
    assert GRAPH == original


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
