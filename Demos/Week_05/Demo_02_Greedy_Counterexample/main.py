"""A bounded exhaustive reference challenges a greedy optimality claim."""

from console_style import print_color
from reference_solver import find_best_change


def validate(denominations, target):
    """Validate the small-input contract and return distinct largest-first coins."""
    if type(target) is not int or not 0 <= target <= 12:
        raise ValueError(
            "target must be an integer from 0 through 12 for this small reference"
        )
    if not denominations or any(
        type(coin) is not int or coin <= 0 for coin in denominations
    ):
        raise ValueError("denominations must be nonempty positive integers")
    return sorted(set(denominations), reverse=True)


def greedy_change(denominations, target):
    """Choose the largest fitting coins, returning None if the amount is incomplete."""
    coins = validate(denominations, target)
    chosen, remaining = [], target
    for coin in coins:
        while remaining >= coin:
            chosen.append(coin)
            remaining -= coin
    return chosen if remaining == 0 else None


def exhaustive_change(denominations, target):
    """Return a minimum-coin result using the supplied bounded reference helper."""
    coins = validate(denominations, target)
    return find_best_change(coins, target, 0)


def main():
    """Compare the greedy claim with bounded exhaustive answers on four cases."""
    print_color(
        "\n===================================================================",
        "heading",
    )
    print_color(
        "GREEDY COUNTEREXAMPLE: minimize coin count, unlimited coins", "heading"
    )
    print_color(
        "===================================================================", "heading"
    )
    for coins, target in (([1, 3, 4], 6), ([3, 4], 6), ([2, 4], 3), ([1, 5, 10], 12)):
        greedy = greedy_change(coins, target)
        best = exhaustive_change(coins, target)
        print(f"\nDenominations={coins}, target={target}")
        print("  Largest-first:", greedy, "(None means no complete greedy result)")
        print("  Exhaustive minimum:", best)
    print("\n4+1+1 uses 3 coins; 3+3 uses 2. Largest-first is not universally optimal.")
    print("A greedy failure also need not mean no solution exists.")


if __name__ == "__main__":
    main()
