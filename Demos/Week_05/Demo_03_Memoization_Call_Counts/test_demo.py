"""Regression checks, separate from the classroom application."""

from contextlib import redirect_stdout
from io import StringIO

from main import (
    cached_fibonacci,
    uncached_fibonacci,
)


def self_check():
    """Check independent answers, counter meanings, input limits, and fresh caches."""
    expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                       233, 377, 610, 987, 1597, 2584, 4181, 6765]
    for n, expected in enumerate(expected_values):
        assert uncached_fibonacci(n)[0] == cached_fibonacci(n)[0] == expected
    assert uncached_fibonacci(5)[1] == 15
    result, calls, hits, cache = cached_fibonacci(5)
    assert (result, calls, hits, len(cache)) == (5, 9, 3, 6)
    assert cache == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    cache[5] = 999
    again = cached_fibonacci(5)
    assert again[:3] == (5, 9, 3)
    assert again[3] is not cache and again[3][5] == 5
    trace_output = StringIO()
    with redirect_stdout(trace_output):
        traced = cached_fibonacci(3, trace=True)
    assert traced[:3] == (2, 5, 1)
    trace_lines = trace_output.getvalue().splitlines()
    assert "TRACE: cache hit F(1) = 1" in trace_lines
    assert [
        line for line in trace_lines if line.startswith("TRACE: store")
    ] == [
        "TRACE: store F(1) = 1; cache={1: 1}",
        "TRACE: store F(0) = 0; cache={1: 1, 0: 0}",
        "TRACE: store F(2) = 1; cache={1: 1, 0: 0, 2: 1}",
        "TRACE: store F(3) = 2; cache={1: 1, 0: 0, 2: 1, 3: 2}",
    ]
    for algorithm in [uncached_fibonacci, cached_fibonacci]:
        for invalid in (-1, True, 21, 2.5, "5"):
            try:
                algorithm(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError("invalid recurrence input accepted")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
