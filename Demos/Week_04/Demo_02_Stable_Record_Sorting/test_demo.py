"""Regression checks, separate from the classroom application."""

from main import (
    battery_key,
    fixture,
    id_key,
    insertion_sort,
    merge_sorted,
)


def self_check():
    """Check stable sorting, counted work, unchanged input order, and merging."""
    rows = fixture()
    result, comparisons, moves, _ = insertion_sort(rows, battery_key)
    assert [row["id"] for row in result] == ["D", "B", "A", "C"]
    assert [row["id"] for row in rows] == ["A", "B", "C", "D"]
    assert result == sorted(rows, key=battery_key)
    assert comparisons == 5 and moves == 4
    assert insertion_sort([], battery_key)[0] == []
    assert insertion_sort(result, battery_key)[0] == result
    assert insertion_sort(list(reversed(result)), battery_key)[0] == sorted(
        reversed(result), key=battery_key)
    assert insertion_sort(rows, id_key)[0] == sorted(rows, key=id_key)
    assert merge_sorted([1, 4], [2, 3]) == [1, 2, 3, 4]


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
