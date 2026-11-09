"""Regression checks, separate from the classroom application."""

from main import (
    exhaustive_change,
    greedy_change,
)


def self_check():
    """Check counterexamples, impossible targets, and independently expected minima."""
    assert greedy_change([1, 3, 4], 6) == [4, 1, 1]
    assert exhaustive_change([1, 3, 4], 6) == [3, 3]
    assert greedy_change([3, 4], 6) is None
    assert exhaustive_change([3, 4], 6) == [3, 3]
    assert exhaustive_change([2, 4], 3) is None
    assert greedy_change([1], 0) == exhaustive_change([1], 0) == []
    assert exhaustive_change([1, 5, 10], 12) == [10, 1, 1]
    minimum_counts = [0, 1, 2, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    for target in range(13):
        solution = exhaustive_change([1, 3, 4], target)
        assert sum(solution) == target
        assert len(solution) == minimum_counts[target]
    assert exhaustive_change([4, 3, 3, 1], 6) == [3, 3]
    assert exhaustive_change([4], 8) == [4, 4]
    assert exhaustive_change([4], 7) is None


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
