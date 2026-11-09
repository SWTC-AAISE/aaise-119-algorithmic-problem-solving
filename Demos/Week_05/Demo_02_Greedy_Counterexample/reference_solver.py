"""Supplied small-input exhaustive reference; focus classroom coding on greedy."""


def find_best_change(coins, remaining, start):
    """Return the shortest completion using validated coins from start onward."""
    if remaining == 0:
        return []

    best = None
    for position in range(start, len(coins)):
        coin = coins[position]
        if coin <= remaining:
            # Reusing this position permits another coin of the same value.
            # Starting here avoids permutations of the same coin combination.
            rest = find_best_change(coins, remaining - coin, position)
            if rest is not None:
                candidate = [coin]
                candidate.extend(rest)
                if best is None or len(candidate) < len(best):
                    best = candidate
    # Each call returns its result; no enclosing variable or shared best is used.
    return best
