"""Supplied human-readable reports and Thursday-only command-line wiring."""

import argparse
from coin_cases import CASES
from console_style import print_color
from investigation_support import exhaustive_change, uncached_fibonacci, cached_fibonacci, validate_n


def describe_payment(payment):
    """Describe an exact payment without displaying a raw collection."""
    if payment is None:
        return "No exact payment produced"
    if not payment:
        return "No coins needed (amount is zero)"
    parts = []
    for coin in payment:
        parts.append(str(coin))
    return " + ".join(parts) + f" ({len(payment)} coins)"


def show_change_cases(greedy_change):
    """Show usable payment choices and distinguish three different outcomes."""
    print_color("EXACT PAYMENT PLANNER", "heading")
    print("Goal: pay the exact amount using as few coins as possible.")
    print("Unlimited coins of each listed value are available.")
    for case in CASES:
        print_color("\n" + case["label"], "heading")
        values = []
        for coin in case["coins"]:
            values.append(str(coin))
        print("Available coin values: " + ", ".join(values))
        print(f"Amount to pay: {case['target']}")
        greedy = greedy_change(case["coins"], case["target"])
        best = exhaustive_change(case["coins"], case["target"])
        print("Largest-first choice: " + describe_payment(greedy))
        print("Fewest-coin reference: " + describe_payment(best))
        if best is None:
            print_color("No exact payment exists with these coins.", "caution")
        elif greedy is None:
            print_color("An exact payment exists, but largest-first missed it.", "caution")
        elif len(greedy) > len(best):
            print_color("Largest-first pays exactly, but uses extra coins.", "caution")
        else:
            print_color("Largest-first matches the minimum count for this case.", "success")


def read_n():
    """Supply Thursday's single bounded argument, its default, and help text."""
    parser = argparse.ArgumentParser(description="AL07: bounded Fibonacci comparison")
    parser.add_argument("--n", type=int, default=8, help="Fibonacci input, 0-20 (default: 8)")
    args = parser.parse_args()
    try:
        validate_n(args.n)
    except ValueError as error:
        parser.error(str(error))
    return args.n


def show_memoization(n, calculate_cached):
    """Separate the unchanged recurrence answer from optional teaching evidence."""
    result, plain_calls = uncached_fibonacci(n)
    cached_result, calls, hits, cache = cached_fibonacci(n, calculate_cached)
    print_color("\nRECURRENCE CHECK", "heading")
    print(f"Fibonacci value at position {n}: {result}")
    print(f"Value using saved answers: {cached_result}")
    print_color("How the calculation reused work", "heading")
    print(f"Function calls without saved answers: {plain_calls}")
    print(f"Function calls with saved answers: {calls}")
    print(f"Calls that found an answer already saved: {hits}")
    print(f"Distinct inputs saved: {len(cache)}")
    print("Both runs start fresh. Calls include hits; these are counts, not timings.")


def run(greedy_change, calculate_cached, enable_memoization):
    """Run Tuesday independently and add Thursday's comparison only when ready."""
    # No parser prerequisite on Tuesday; the Thursday stage introduces --n.
    n = None
    if enable_memoization:
        n = read_n()
    show_change_cases(greedy_change)
    if enable_memoization:
        show_memoization(n, calculate_cached)
