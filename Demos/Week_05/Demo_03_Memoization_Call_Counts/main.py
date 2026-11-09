"""Compare recursive work with and without explicit, fresh-run memoization."""

import argparse
from console_style import print_color


def validate(n):
    """Keep the supplied comparison within nonnegative integer inputs 0–20."""
    if type(n) is not int or not 0 <= n <= 20:
        raise ValueError("n must be an integer from 0 through 20 for the live demo")


def calculate_uncached(n, counts):
    """Calculate a validated Fibonacci input and count every helper invocation."""
    counts["calls"] += 1
    if n < 2:
        return n
    previous = calculate_uncached(n - 1, counts)
    earlier = calculate_uncached(n - 2, counts)
    return previous + earlier


def uncached_fibonacci(n):
    """Return the Fibonacci result and call count using fresh counter state."""
    validate(n)
    counts = {"calls": 0}
    result = calculate_uncached(n, counts)
    return result, counts["calls"]


def calculate_cached(n, cache, counts):
    """Reuse a saved result or compute and store it, counting calls and hits."""
    counts["calls"] += 1
    if n in cache:
        counts["hits"] += 1
        return cache[n]
    if n < 2:
        result = n
    else:
        previous = calculate_cached(n - 1, cache, counts)
        earlier = calculate_cached(n - 2, cache, counts)
        result = previous + earlier
    cache[n] = result
    return result


def cached_fibonacci(n):
    """Return the result, calls, hits, and an independent cache for this run."""
    validate(n)
    cache = {}
    counts = {"calls": 0, "hits": 0}
    result = calculate_cached(n, cache, counts)
    return result, counts["calls"], counts["hits"], cache


def main():
    """Read the bounded input and present equivalent answers with call evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10, help="Fibonacci input, 0–20 (default: 10)")
    args = parser.parse_args()
    try:
        validate(args.n)
    except ValueError as error:
        parser.error(str(error))
    print_color(
        "\n===================================================================",
        "heading",
    )
    print_color("MEMOIZATION: reuse an answer already calculated", "heading")    print_color(
        "===================================================================\n",
        "heading",
    )
    result, plain_calls = uncached_fibonacci(args.n)
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
