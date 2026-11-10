"""
Beginner's guide to the exhaustive coin-change reference function.

The function below finds a way to make `remaining` using the coins at or after
`start`, and returns the way that uses the fewest coins. For example, with
coins [4, 3, 1] and a target of 6, it compares possible combinations and finds
[3, 3]. This is better than the largest-first choice [4, 1, 1].

How to read the function:

1. If no amount remains, this branch has succeeded; return an empty list.
   The caller adds the coin it chose to that list.
2. Try each coin from `start` onward. Skip coins larger than the amount left.
3. For a coin that fits, solve the smaller amount left after using it.
   Pass that coin's position as the next `start`, so it may be reused.
4. If the smaller amount can be completed, put this coin in front of that
   completion. Keep the candidate only if it uses fewer coins than the best
   candidate found so far.
5. Return the best candidate, or None if no combination can finish the amount.

For the [4, 3, 1] coins and target 6, the important branches are:

    Choose 4: the remaining 2 can be made as [1, 1], giving [4, 1, 1].
    Choose 3: the remaining 3 can be made as [3], giving [3, 3].

The function compares these results, then also checks combinations starting
with 1. It returns [3, 3], the complete solution with the fewest coins.

The `start` position avoids trying the same combination in different orders.
For example, [4, 3] and [3, 4] use the same coins, so the function only needs
to consider one of those orders. Starting again at the chosen position (rather
than the next one) still allows unlimited copies of a coin.

This helper expects positive coin values and a nonnegative amount. In the demo,
the caller validates the input and supplies distinct coins. The small target
limit in the demo keeps this exhaustive search practical; this approach can be
slow for larger targets because it explores many combinations.
"""


def find_best_change(coins, remaining, start):
    """Return the fewest coins that complete `remaining`, or None if impossible."""
    # A remaining amount of zero means this branch found a complete solution.
    # The empty list is correct here: this call itself did not choose a coin.
    if remaining == 0:
        return []

    # Each call keeps its own best answer. None means no complete answer has
    # been found yet for this particular remaining amount and start position.
    best = None

    # Only use this coin or a later one. This keeps combinations in one order
    # and prevents duplicate searches such as [4, 3] and [3, 4].
    for position in range(start, len(coins)):
        coin = coins[position]

        # A coin bigger than the amount left cannot be part of this solution.
        if coin <= remaining:
            # Recursively solve the smaller problem after using this coin.
            # Keep the same position available, because coins can be reused.
            rest = find_best_change(coins, remaining - coin, position)

            # None means the smaller amount could not be completed, so this
            # choice cannot become a complete solution either.
            if rest is not None:
                # Build a new list for this candidate: this coin plus the
                # successful solution returned by the recursive call.
                candidate = [coin]
                candidate.extend(rest)

                # Compare the number of coins, not their values. Replace the
                # current answer only when this complete candidate is shorter.
                if best is None or len(candidate) < len(best):
                    best = candidate

    # The loop checked every allowed first coin. Return the shortest complete
    # result, or None if none of those choices could finish the amount.
    return best
