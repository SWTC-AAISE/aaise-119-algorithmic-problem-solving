"""Separate checks for qualitative workload examples."""

from copy import deepcopy
import main as explicit
import main2 as compact


def self_check():
    """Verify lookup parity, ordering, counts, and unchanged input records."""
    records = [{"id": 0}, {"id": 1}, {"id": 2}, {"id": 3}]
    before = deepcopy(records)
    for queries, expected, count in (([0], [records[0]], 1),
                                     ([0, 3, -1] * 2, [records[0], records[3], None] * 2, 18),
                                     ([], [], 0)):
        assert explicit.scan(records, queries) == (expected, count)
        assert explicit.indexed(records, queries) == compact.indexed(records, queries) == expected
    assert explicit.scan([], [0]) == ([None], 0)
    assert compact.indexed([], [0]) == [None]
    assert records == before
    assert explicit.scan([records[0], {}], [0]) == ([records[0]], 1)
    for size in (0, 1, 4):
        assert explicit.make_records(size) == compact.make_records(size)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
