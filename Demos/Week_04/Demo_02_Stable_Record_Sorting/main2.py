"""Documented companion to main.py; sorting and output are unchanged.

Tuesday reuses Monday's named keys and teaches stable insertion sorting.
The comments explain movement, equality, counted units, and shallow list views.
Compact syntax is documented for review, not expanded into new algorithm scope.
"""


def battery_key(record):
    """Select the battery value used for ordering without editing a record."""
    return record["battery"]


def id_key(record):
    """Select an alternative key while keeping the sorting algorithm unchanged."""
    return record["id"]


def insertion_sort(records, key):
    """Return (ordered view, comparisons, right-shifts, trace), preserving equal-key order.

    The outer list is new; record dictionaries are shared. This function reorders
    references but does not edit record fields or mutate the input list's order.
    Counts describe this tiny worked example, not wall-clock measurements.
    """
    ordered = list(records)
    # Chained assignment: initialize both integer counters to zero.
    # Integers are immutable; increasing one counter later does not change the other.
    comparisons = moves = 0
    trace = []
    # The one-item prefix is already sorted. Each iteration inserts the next
    # record into that prefix, extending the sorted portion by one position.
    for position in range(1, len(ordered)):
        item = ordered[position]
        previous = position - 1
        while previous >= 0:
            comparisons += 1
            # Equality stops movement: the earlier equal-key record stays before
            # item. Using < here would shift equal items and lose stability.
            if key(ordered[previous]) <= key(item):
                break
            # Shift the larger prior reference right to open an insertion slot.
            # item still holds the reference being inserted, so it is not lost.
            ordered[previous + 1] = ordered[previous]
            moves += 1
            previous -= 1
        # previous may be -1; adding one then places item at position zero.
        # This final placement is NOT counted as a right-shift in this demo.
        ordered[previous + 1] = item
        # A new list of ID strings captures order after this insertion. The
        # comprehension is display/trace support, not another sorting algorithm.
        trace.append([row["id"] for row in ordered])
    return ordered, comparisons, moves, trace


def merge_sorted(left, right):
    """Combine two already sorted number lists as a guided merge contrast.

    This is a merge step, not a recursive merge-sort implementation and not
    a claim about the algorithm used by Python's sorted().
    """
    # Parallel assignment: result gets []; i and j each get 0.
    # Unlike chained assignment, the three targets receive corresponding values.
    # i and j track positions in the two already sorted input lists.
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # [i:] and [j:] mean the remaining suffixes. At least one is empty here.
    # + joins lists into a new result rather than mutating either input.
    return result + left[i:] + right[j:]


def fixture():
    """Create a small shuffled list where A and C share battery 70."""
    return [
        {"id": "A", "battery": 70},
        {"id": "B", "battery": 50},
        {"id": "C", "battery": 70},
        {"id": "D", "battery": 30},
    ]


def main():
    """Show stable insertion steps, changed-key reuse, and the supplied merge step."""
    print("STABLE RECORD SORTING: ascending battery; input list is not mutated")
    print(
        "Callable key contract: battery_key or id_key; the sorting loop stays unchanged."
    )
    rows = fixture()
    # Each tuple presents one ID/battery pair; the comprehension collects them.
    print("Input:", [(row["id"], row["battery"]) for row in rows])
    ordered, comparisons, moves, trace = insertion_sort(rows, battery_key)
    # enumerate(trace, 1) numbers the DISPLAYED insertion steps from 1.
    # It does not change the algorithm's zero-based list positions.
    for step, state in enumerate(trace, 1):
        print(f"Insertion {step}: {state}")
    print("Result:", [row["id"] for row in ordered])
    print(
        f"Key comparisons: {comparisons}; right-shifts: {moves} (final placement not counted)"
    )
    print(
        "Equal-key A/C retain input order; an ID tie-breaker is not the same concept."
    )
    # Repeated _ names intentionally ignore the other three returned results.
    # Passing a different named key changes the order, not the insertion loop.
    id_ordered, _, _, _ = insertion_sort(rows, id_key)
    print(
        "Changed key, same algorithm: ID order =", [id_key(row) for row in id_ordered]
    )
    print("Guided merge contrast: [1, 4] + [2, 3] ->", merge_sorted([1, 4], [2, 3]))
    # Library parity is checked separately in test_demo.py. No timer, benchmark
    # harness, extra sorting implementation, or copy engine is added here.


if __name__ == "__main__":
    main()
