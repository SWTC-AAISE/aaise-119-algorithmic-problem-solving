"""Supplied validation, reference, recurrence, and fresh-run counter wiring."""

from reference_solver import find_best_change


def validate_change(denominations, target):
    """Validate bounded inputs and return distinct coins in largest-first order."""
    if type(target) is not int or not 0 <= target <= 12:
        raise ValueError("target must be an integer from 0 through 12")
    if not isinstance(denominations, list) or not denominations:
        raise ValueError("denominations must be a nonempty list")
    for coin in denominations:
        if type(coin) is not int or coin <= 0:
            raise ValueError("coin values must be positive integers")
    return sorted(set(denominations), reverse=True)


def exhaustive_change(denominations, target):
    """Return a minimum-coin answer or None using the supplied tiny-input solver."""
    coins = validate_change(denominations, target)
    return find_best_change(coins, target, 0)


def validate_n(n):
    """Keep the recursive comparison within integer inputs zero through twenty."""
    if type(n) is not int or not 0 <= n <= 20:
        raise ValueError("n must be an integer from 0 through 20")


def calculate_uncached(n, counts):
    """Calculate the supplied recurrence and count every function invocation."""
    counts["calls"] += 1
    if n < 2:
        return n
    previous = calculate_uncached(n - 1, counts)
    earlier = calculate_uncached(n - 2, counts)
    return previous + earlier


def uncached_fibonacci(n):
    """Return the supplied Fibonacci answer and a fresh call count."""
    validate_n(n)
    counts = {"calls": 0}
    result = calculate_uncached(n, counts)
    return result, counts["calls"]


def cached_fibonacci(n, calculate_cached):
    """Run the student's helper with a new empty cache and counters each time."""
    validate_n(n)
    cache = {}
    counts = {"calls": 0, "hits": 0}
    result = calculate_cached(n, cache, counts)
    return result, counts["calls"], counts["hits"], cache
