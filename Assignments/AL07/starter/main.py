"""Optional AL07 scaffold: Tuesday payment choices, Thursday saved answers."""

from investigation_support import validate_change
from investigation_display import run

ENABLE_MEMOIZATION = False  # Change to True after Thursday's helper works.


# TUESDAY — Implement the local choice; the reference solver is supplied.
def greedy_change(denominations, target):
    """Return largest-first exact change, or None when that choice gets stuck."""
    coins = validate_change(denominations, target)
    # Keep chosen coins and the amount still unpaid.
    # Consider the supplied largest-first coin order.
    # Keep using a coin while it fits the unpaid amount.
    # Return the chosen coins for an exact payment, including [] for zero.
    # Return None if an unpaid amount remains. Do not change denominations.
    raise NotImplementedError("Complete the largest-first payment rule.")


# THURSDAY — The recurrence and counters are supplied; add lookup and storage.
def calculate_cached(n, cache, counts):
    """Return F(n), reusing saved answers while counting all calls and hits."""
    counts["calls"] += 1
    # Before computing, check whether this input already has a saved answer.
    # A saved zero is still an answer. Count a hit and return that saved value.
    if n < 2:
        result = n
    else:
        previous = calculate_cached(n - 1, cache, counts)
        earlier = calculate_cached(n - 2, cache, counts)
        result = previous + earlier
    # Save the result under this input, including base-case results.
    return result


def main():
    """Present the completed stages using the supplied driver and reports."""
    run(greedy_change, calculate_cached, ENABLE_MEMOIZATION)


if __name__ == "__main__":
    main()
