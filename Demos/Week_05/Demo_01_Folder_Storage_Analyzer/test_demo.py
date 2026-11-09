"""Separate checks for storage totals, equivalent traversal, and input preservation."""

from copy import deepcopy
from main import recursive_total, iterative_total
from folder_data import COURSE_FILES


def self_check():
    """Check known subtotals, additional nesting, malformed data, and unchanged input."""
    original = deepcopy(COURSE_FILES)
    week = COURSE_FILES["items"][1]
    activities = week["items"][1]
    empty = {"type": "folder", "name": "Empty", "items": []}
    zero = {"type": "file", "name": "empty.txt", "size_mb": 0}
    flat = {
        "type": "folder", "name": "Flat",
        "items": [zero, {"type": "file", "name": "small.pdf", "size_mb": 3}],
    }
    extra_level = {"type": "folder", "name": "Archive", "items": [COURSE_FILES, empty]}
    for algorithm in [recursive_total, iterative_total]:
        for item, expected in [(COURSE_FILES, 20), (week, 16), (activities, 10),
                               (empty, 0), (zero, 0), (flat, 3), (extra_level, 20)]:
            assert algorithm(item) == expected
        malformed = [
            True,
            {"name": "Missing type"},
            {"type": "folder", "name": "Bad folder", "items": None},
            {"type": "file", "name": "Negative", "size_mb": -1},
            {"type": "file", "name": "Boolean", "size_mb": True},
            {"type": "file", "name": "Fraction", "size_mb": 1.5},
            {"type": "folder", "name": "Bad child", "items": [None]},
        ]
        for item in malformed:
            try:
                algorithm(item)
            except ValueError:
                pass
            else:
                raise AssertionError("Malformed folder data must be rejected.")
    assert COURSE_FILES == original


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
