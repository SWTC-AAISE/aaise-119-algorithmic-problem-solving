"""Regression checks, separate from the classroom application."""

from main import (
    halving_trace,
    indexed_lookup,
    scan_lookup,
    first_record,
)
import main2 as compact
from copy import deepcopy


def self_check():
    """Check counts, equivalent syntax, query order, and unchanged inputs."""
    for size in (4, 8, 16, 32):
        records = [{"id": value} for value in range(size)]
        queries = [-1] * size
        assert scan_lookup(records, queries)[0] == indexed_lookup(records, queries)[0]
    rows = [{"id": value} for value in range(4)]
    result, count = scan_lookup(rows, [0, 3, -1])
    assert count == 9 and result == [rows[0], rows[3], None]
    assert indexed_lookup(rows, [0, 3, -1])[0] == result
    assert scan_lookup([], [0]) == ([None], 0)
    assert halving_trace(16) == [16, 8, 4, 2, 1]
    assert first_record(rows) is rows[0]
    assert first_record([]) is None
    for size in (0, 1, 4, 32):
        assert compact.make_records(size) == [{"id": value} for value in range(size)]
    for records, queries in (([], []), ([], [1]), (rows, []),
                             (rows, [3, -1, 0, 3]), (rows, [-1, -1])):
        before = deepcopy(records)
        assert compact.indexed_lookup(records, queries) == indexed_lookup(records, queries)
        assert scan_lookup(records, queries)[0] == compact.indexed_lookup(records, queries)[0]
        assert records == before
    # A first match must stop before inspecting the deliberately unusable next row.
    assert scan_lookup([{"id": 0}, {}], [0]) == ([{"id": 0}], 1)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
