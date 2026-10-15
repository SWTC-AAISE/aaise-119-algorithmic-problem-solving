"""Separate checks for recognition examples and equivalent code forms."""

from copy import deepcopy
import main as explicit
import main2 as compact


def self_check():
    """Verify independent first-match answers, counts, and unchanged inputs."""
    for size in (0, 1, 4, 8):
        assert explicit.make_records(size) == compact.make_records(size)
    records = [{"id": 0}, {"id": 1}, {"id": 2}, {"id": 3}]
    before = deepcopy(records)
    for target, expected, count in ((0, records[0], 1), (1, records[1], 2),
                                    (3, records[3], 4), (-1, None, 4)):
        assert explicit.find_record(records, target) == expected
        assert compact.find_record(records, target) == expected
        assert explicit.scan_case(records, target) == (expected, count)
    assert explicit.scan_case([], -1) == (None, 0)
    assert compact.find_record([], -1) is None
    for lookup in (explicit.find_record, compact.find_record):
        assert lookup([records[0], {}], 0) is records[0]
    assert records == before


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
