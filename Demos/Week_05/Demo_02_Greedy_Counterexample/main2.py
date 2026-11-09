"""Documented equivalent of main.py; algorithms, cases, and output are unchanged.

A greedy strategy takes the best-looking next step without reconsidering it.
This example asks whether repeatedly choosing the largest fitting coin always
minimizes the number of coins. A supplied exhaustive solver checks that claim
on small inputs; students do not need to implement its search machinery here.
"""

# The reference helper is a top-level function in another module.
# Its inputs are passed explicitly and its answer is returned to the caller.
from reference_solver import find_best_change


def validate(denominations, target):
    """Validate the small-input contract and return distinct largest-first coins."""
    # The 0–12 bound keeps the supplied exhaustive comparison small.
    # Exact type checking rejects True/False, which Python otherwise treats as integers.
    if type(target) is not int or not 0 <= target <= 12:
        raise ValueError("target must be an integer from 0 through 12 for this small reference")
    # A denomination is an available coin VALUE, not the number of coins available.
    # There must be at least one value, and every value must be a positive integer.
    # any(...) checks whether at least one value violates that rule.
    if not denominations or any(type(coin) is not int or coin <= 0 for coin in denominations):
        raise ValueError("denominations must be nonempty positive integers")
    # set removes duplicate values; sorted puts the largest value first.
    # This creates a new list rather than reordering the caller's input list.
    return sorted(set(denominations), reverse=True)


def greedy_change(denominations, target):
    """Choose the largest fitting coins, returning None if the amount is incomplete."""
    coins = validate(denominations, target)
    # Parallel assignment: chosen starts empty; remaining starts at the requested amount.
    chosen, remaining = [], target
    for coin in coins:
        # Keep taking this value while it fits: the supply of each coin is unlimited.
        # Once we move to a smaller value, we never undo an earlier choice.
        while remaining >= coin:
            chosen.append(coin)
            remaining -= coin
    # A complete result must reach the exact target; a partial amount is not success.
    # This conditional expression returns chosen on success and None otherwise.
    # Target zero succeeds with [], meaning no coins are needed.
    return chosen if remaining == 0 else None


def exhaustive_change(denominations, target):
    """Return a minimum-coin result using the supplied bounded reference helper."""
    # Apply the same input rules so the two strategies solve the same problem.
    coins = validate(denominations, target)
    # The helper considers allowed combinations and returns a shortest completion.
    # Zero starts at the first position in the prepared coin-value list.
    # The helper returns None only when no complete combination exists.
    return find_best_change(coins, target, 0)


def main():
    """Compare the greedy claim with bounded exhaustive answers on four cases."""
    print("GREEDY COUNTEREXAMPLE: minimize coin count, unlimited coins")
    # Each pair holds (available coin values, requested amount).
    # 1: greedy completes the amount but uses too many coins.
    # 2: greedy gets stuck even though a complete solution exists.
    # 3: the amount is impossible with these coin values.
    # 4: both strategies return a minimum-coin answer on this case.
    for coins, target in (([1, 3, 4], 6), ([3, 4], 6), ([2, 4], 3), ([1, 5, 10], 12)):
        greedy = greedy_change(coins, target)
        best = exhaustive_change(coins, target)
        print(f"\nDenominations={coins}, target={target}")
        print("  Largest-first:", greedy, "(None means no complete greedy result)")
        print("  Exhaustive minimum:", best)
    # One counterexample disproves the claim that largest-first ALWAYS minimizes coins.
    # It does not establish that every greedy strategy fails on every problem.
    print("\n4+1+1 uses 3 coins; 3+3 uses 2. Largest-first is not universally optimal.")
    print("A greedy failure also need not mean no solution exists.")


if __name__ == "__main__":
    main()
