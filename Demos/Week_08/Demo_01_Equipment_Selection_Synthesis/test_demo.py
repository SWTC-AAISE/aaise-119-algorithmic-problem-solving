"""Independent expected-result checks, separate from ordinary loan reports."""

from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
import main
import main2


def result_ids(results):
    """Make request order and unsuccessful results visible in assertions."""
    ids = []
    for row in results:
        if row is None:
            ids.append(None)
        else:
            ids.append(row["id"])
    return ids


def check_methods(module):
    """Check both approaches against independently specified loan decisions."""
    rows = deepcopy(module.EQUIPMENT)
    queries = ["E01", "E02", "E03", "E04", "E99"]
    original_rows = deepcopy(rows)
    original_queries = list(queries)
    for lookup in [module.scan_requests, module.indexed_requests]:
        baseline = lookup(rows, queries, 50)
        assert result_ids(baseline) == ["E01", None, None, "E04", None]
        assert baseline == [original_rows[0], None, None, original_rows[3], None]
        revised = lookup(rows, queries, 80)
        assert result_ids(revised) == ["E01", None, None, None, None]
        assert revised == [original_rows[0], None, None, None, None]
        assert result_ids(lookup(rows, queries, 0)) == ["E01", None, None, "E04", None]
        assert lookup(rows, queries, 100) == [None, None, None, None, None]
        assert lookup([], queries, 50) == [None, None, None, None, None]
        assert lookup(rows, [], 50) == []
        repeated = ["E04", "E01", "E04", "E99", "E02"]
        assert result_ids(lookup(rows, repeated, 50)) == ["E04", "E01", "E04", None, None]
        assert rows == original_rows
        assert queries == original_queries


def check_boundaries(module):
    """Check inclusive battery boundaries without relaxing type or availability."""
    cases = [
        (49, ["E04", "E01"]),
        (50, ["E04", "E01"]),
        (51, [None, "E01"]),
        (79, [None, "E01"]),
        (80, [None, "E01"]),
        (81, [None, None]),
    ]
    for lookup in [module.scan_requests, module.indexed_requests]:
        for threshold, expected in cases:
            actual = lookup(module.EQUIPMENT, ["E04", "E01"], threshold)
            assert result_ids(actual) == expected
    assert module.eligible(module.EQUIPMENT[0], 80) is True
    assert module.eligible(module.EQUIPMENT[3], 51) is False
    assert module.eligible(module.EQUIPMENT[1], 0) is False
    assert module.eligible(module.EQUIPMENT[2], 0) is False


def capture_output(module):
    """Run the default presentation without changing the shared fixture."""
    original = deepcopy(module.EQUIPMENT)
    requests = list(module.REQUESTS)
    output = StringIO()
    with redirect_stdout(output):
        module.main()
    assert module.EQUIPMENT == original
    assert module.REQUESTS == requests
    return output.getvalue()


def self_check():
    """Check independent expectations, state preservation and annotated parity."""
    check_methods(main)
    check_boundaries(main)
    check_methods(main2)
    check_boundaries(main2)
    output = capture_output(main)
    assert capture_output(main2) == output
    assert "Cedar laptop: READY TO LOAN (80%)" in output
    assert "Birch laptop: Battery 50%; needs at least 80%" in output
    assert "Maple laptop: Already checked out" in output
    assert "Studio tablet: This request needs a laptop" in output
    assert "E99: No equipment found with this ID" in output


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed for main.py and main2.py.")
