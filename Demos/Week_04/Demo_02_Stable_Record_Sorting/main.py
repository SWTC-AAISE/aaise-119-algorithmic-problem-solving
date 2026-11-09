"""Stable insertion sorting with comparison/move counts and a merge contrast."""


def battery_key(record):
    """Select the battery value used to order an equipment record."""
    return record["battery"]


def id_key(record):
    """Select the ID as an alternative ordering key."""
    return record["id"]


def insertion_sort(records, key):
    """Return a stable ordered view, comparison count, right-shifts, and ID trace."""
    ordered = list(records)
    # Chained assignment: initialize both integer counters to zero.
    comparisons = moves = 0
    trace = []
    for position in range(1, len(ordered)):
        item = ordered[position]
        previous = position - 1
        while previous >= 0:
            comparisons += 1
            if key(ordered[previous]) <= key(item):
                break
            ordered[previous + 1] = ordered[previous]
            moves += 1
            previous -= 1
        ordered[previous + 1] = item
        trace.append([row["id"] for row in ordered])
    return ordered, comparisons, moves, trace


def merge_sorted(left, right):
    """Merge two already sorted number lists as a guided contrast."""
    # Parallel assignment: result gets []; i and j each get 0.
    result, i, j = [], 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def fixture():
    """Provide four records with an equal-battery pair for stability checks."""
    return [
        {"id": "A", "battery": 70},
        {"id": "B", "battery": 50},
        {"id": "C", "battery": 70},
        {"id": "D", "battery": 30},
    ]


def main():
    """Show insertion-sort steps, stable ties, changed keys, and a merge contrast."""
    print("\n===================================================================")
    print("STABLE RECORD SORTING: ascending battery; input list is not mutated")
    print("===================================================================\n")

    print(
        "Callable key contract: battery_key or id_key; the sorting loop stays unchanged.\n"
    )
    rows = fixture()
    print("Input:", [(row["id"], row["battery"]) for row in rows])
    ordered, comparisons, moves, trace = insertion_sort(rows, battery_key)
    for step, state in enumerate(trace, 1):
        print(f"Insertion {step}: {state}")
    print("Result:", [row["id"] for row in ordered])
    print(
        f"Key comparisons: {comparisons}; right-shifts: {moves} (final placement not counted)"
    )
    print(
        "Equal-key A/C retain input order; an ID tie-breaker is not the same concept."
    )
    id_ordered, _, _, _ = insertion_sort(rows, id_key)
    print(
        "Changed key, same algorithm: ID order =", [id_key(row) for row in id_ordered]
    )
    print("Guided merge contrast: [1, 4] + [2, 3] ->", merge_sorted([1, 4], [2, 3]))


if __name__ == "__main__":
    main()
