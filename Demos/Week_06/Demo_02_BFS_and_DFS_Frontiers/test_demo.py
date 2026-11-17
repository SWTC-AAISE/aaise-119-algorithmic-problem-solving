"""Instructor checks for traversal behavior; unusual cases are not another lesson."""

from copy import deepcopy
from contextlib import redirect_stdout
from io import StringIO
import main
import main2
from main import GRAPH, breadth_first, depth_first, traverse
from graph_display import show_frontier


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


def check_frontier_tables():
    """Check compact tables, real DFS duplicates, and both entry points."""
    outputs = []
    for module in (main, main2):
        output = StringIO()
        with redirect_stdout(output):
            module.main()
        outputs.append(output.getvalue())
    assert outputs[0] == outputs[1]
    teaching, bfs_table = outputs[0].split("\nBFS queue: FRONT -> REAR\n")
    bfs_table, dfs_table = bfs_table.split("\nDFS stack: BOTTOM -> TOP\n")
    assert "Teaching view - BFS:" in teaching
    assert "Teaching view - DFS:" in teaching
    assert bfs_table.startswith(
        "Removes the front item, then adds newly discovered neighbors at the rear.\n"
        "Step  Processed  Contents\n0     (start)    [Library]\n"
    )
    assert dfs_table.startswith(
        "Removes the top item, then pushes eligible neighbors onto the top.\n"
        "Step  Processed  Contents\n0     (start)    [Library]\n"
    )
    assert "1     Library    [Atrium, Lab]\n" in bfs_table
    assert "5     Studio     []\n" in bfs_table
    assert "1     Library    [Lab, Atrium]\n" in dfs_table
    assert "4     Studio     [Lab, Lab]\n5     Lab        [Lab]\n" in dfs_table
    _, trace, _ = depth_first(GRAPH, "Annex")
    output = StringIO()
    with redirect_stdout(output):
        show_frontier("DFS stack: BOTTOM -> TOP", trace, "Annex",
                      "Removes the top item, then pushes eligible neighbors onto the top.")
    assert "0     (start)    [Annex]\n1     Annex      []\n" in output.getvalue()


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    check_frontier_tables()
    print("Checks passed.")
