"""Documented equivalent of main.py; the same algorithms and output.

Memoization stores the answer for an input so repeated subproblems can reuse it.
The explicit cache belongs to this comparison, not to the browser or Python globally.
"""

import argparse
from console_style import print_color


def validate(n):
    """Keep the supplied comparison within nonnegative integer inputs 0–20."""
    if type(n) is not int or not 0 <= n <= 20:
        raise ValueError("n must be an integer from 0 through 20 for the live demo")


def calculate_uncached(n, counts):
    """Calculate a validated Fibonacci input and count every helper invocation."""
    # Count this helper invocation before checking for a direct or saved answer.
    counts["calls"] += 1
    # F(0)=0 and F(1)=1 can be answered without another recursive call.
    if n < 2:
        return n
    # Repeated input values are recalculated because this version stores no answers.
    previous = calculate_uncached(n - 1, counts)
    earlier = calculate_uncached(n - 2, counts)
    return previous + earlier


def uncached_fibonacci(n):
    """Return the Fibonacci result and call count using fresh counter state."""
    validate(n)
    # The public entry creates a fresh dictionary; recursive calls share this object.
    counts = {"calls": 0}
    result = calculate_uncached(n, counts)
    # Python packs these two results into a tuple for the caller to unpack.
    return result, counts["calls"]


def calculate_cached(n, cache, counts):
    """Reuse a saved result or compute and store it, counting calls and hits."""
    # Count this helper invocation before checking for a direct or saved answer.
    counts["calls"] += 1
    # HIT: this input already has a saved answer; skip its two recursive branches.
    if n in cache:
        counts["hits"] += 1
        return cache[n]
    # F(0)=0 and F(1)=1 can be answered without another recursive call.
    if n < 2:
        result = n
    else:
        # Pass the same cache/counter objects down both branches without copying them.
        # A branch that revisits an input can use an answer saved by an earlier branch.
        previous = calculate_cached(n - 1, cache, counts)
        earlier = calculate_cached(n - 2, cache, counts)
        result = previous + earlier
    # MISS: save the newly obtained answer under its input, including base cases.
    cache[n] = result
    return result


def cached_fibonacci(n):
    """Return the result, calls, hits, and an independent cache for this run."""
    validate(n)
    # Separate initialization replaces the former packed cache/calls/hits assignment.
    # This new cache cannot contain answers left by an earlier comparison.
    cache = {}
    # Named counters make their meanings explicit; each run receives its own state.
    counts = {"calls": 0, "hits": 0}
    result = calculate_cached(n, cache, counts)
    # Return the actual per-run cache so tests can inspect its entries/independence.
    return result, counts["calls"], counts["hits"], cache


def main():
    """Read the bounded input and present equivalent answers with call evidence."""
    # Supplied interface: introduce this wiring in the bounded argparse lesson.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10, help="Fibonacci input, 0–20 (default: 10)")
    # Read the command line; --help is supplied automatically by argparse.
    args = parser.parse_args()
    try:
        # type=int converts the input, while this separate check enforces 0–20.
        validate(args.n)
    except ValueError as error:
        parser.error(str(error))

    print_color("MEMOIZATION: reuse an answer already calculated", "heading")
    # Unpack two returned values; this is assignment syntax, not a caching feature.
    result, plain_calls = uncached_fibonacci(args.n)
    # Run with the same n and unpack four documented results in the same order.
    cached_result, calls, hits, cache = cached_fibonacci(args.n)
    print_color(f"F({args.n})={result}", "success")
    print(f"Answer with memoization: {cached_result}")
    print(f"Calls without memoization: {plain_calls}")
    print(f"Calls with memoization: {calls}")
    print(f"Calls that reused a saved answer: {hits}")
    print(f"Distinct inputs saved in this run: {len(cache)}")
    print("\nBoth results use F(0)=0 and F(1)=1.")
    print("Every comparison starts with a fresh dictionary cache.")
    print("Calls include cache hits; counts describe work, not elapsed time.")


if __name__ == "__main__":
    main()
