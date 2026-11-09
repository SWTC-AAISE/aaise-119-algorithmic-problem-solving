"""Optional AL07 test starting point; expand it with your own expectations."""

from main import greedy_change, calculate_cached
from investigation_support import exhaustive_change, cached_fibonacci, uncached_fibonacci


def test_tuesday():
    """Begin with an independently reasoned payment counterexample."""
    assert greedy_change([1, 4, 6], 8) == [6, 1, 1]
    assert exhaustive_change([1, 4, 6], 8) == [4, 4]
    # Add the gets-stuck-but-reachable, impossible, agreement, zero, and input checks.


def test_thursday():
    """Check saved answers and bounded counts against a hand-checkable input."""
    result, calls, hits, cache = cached_fibonacci(5, calculate_cached)
    assert result == 5
    assert calls == 9
    assert hits == 3
    assert len(cache) == 6
    # Add base cases, another known answer, fresh repeated runs, and invalid n.


if __name__ == "__main__":
    test_tuesday()
    # THURSDAY: uncomment the following call when implementing the cache.
    # test_thursday()
    print("Tuesday starting check passed; expand the tests before submitting.")
