"""Documented companion to main.py; all executable search behavior is unchanged.

Monday progresses through key selection, equality, linear traversal, and ordered
binary traversal. Comments explain the existing syntax rather than introduce
another implementation. Compact expressions remain available for instructor
review; reading this file does not make them additional assessed requirements.
"""


def id_key(record):
    """Select the ID; this function neither searches nor changes the record."""
    return record["id"]


def matches(value, target):
    """Apply the equality rule shared by both search algorithms."""
    return value == target


def compare_values(value, target):
    """Report equality or direction using zero, negative one, or positive one."""
    if matches(value, target):
        return 0
    # Conditional expression: return -1 when value is smaller, otherwise 1.
    # Equality was handled above. This could be written as ordinary if/else.
    # Unlike an eligibility predicate, this tells binary search WHICH half to keep.
    return -1 if value < target else 1


def linear_search(records, target, key=id_key):
    """Return (position, trace), using None for absence without assuming order."""
    trace = []
    # enumerate supplies a zero-based position and its record on each iteration.
    # key is a FUNCTION, defaulting to id_key; it is not the string 'id'.
    for position, record in enumerate(records):
        value = key(record)
        # Each tuple records one observation, not another permanent record ID.
        trace.append((position, value))
        if matches(value, target):
            # A first match ends the scan, even if later keys duplicate this one.
            return position, trace
    # Not-found belongs after the loop so a single nonmatch does not end the scan.
    return None, trace


def binary_search(records, target, key=id_key):
    """Return the same result shape, assuming ascending order under the given key.

    The caller establishes sorting; the function does not scan to verify it on
    every query. Equal keys permit any matching position, not necessarily first.
    """
    # Three names receive three values: inclusive bounds and an empty trace.
    # For an empty list high is -1, so the loop never executes.
    low, high, trace = 0, len(records) - 1, []
    while low <= high:
        # // is floor division: with nonnegative bounds it gives an integer index.
        middle = (low + high) // 2
        value = key(records[middle])
        trace.append((low, high, middle, value))
        comparison = compare_values(value, target)
        if comparison == 0:
            return middle, trace
        if comparison < 0:
            # A smaller midpoint rules out itself AND the lower half, but only
            # because the view is ordered under the SAME key being compared.
            low = middle + 1
        else:
            high = middle - 1
    # Crossing bounds means no candidates remain; None is not position zero.
    return None, trace


def model_key(record):
    """Select a different field without rewriting either traversal algorithm."""
    return record["model"]


def fixture():
    """Create deliberately unsorted ID records for the precondition example."""
    return [{"id": 3, "battery": 20}, {"id": 1, "battery": 80},
            {"id": 2, "battery": 90}]


def main():
    """Demonstrate criteria, traversals, valid order, failure, and duplicate keys."""
    rows = fixture()
    print("SEARCH SCAFFOLD: key -> match -> linear traversal -> ordered binary traversal")
    print("Shared contract: (position in supplied view, trace); None means absent")

    print("\n1. CRITERIA: id_key selects a value; matches defines equality")
    # List comprehension: call id_key for each row and collect its result.
    # This is a compact display projection, not the search implementation.
    print("Input IDs:", [id_key(row) for row in rows])
    print("First record matches ID 3:", matches(id_key(rows[0]), 3))
    print("First record matches ID 99:", matches(id_key(rows[0]), 99))

    print("\n2. LINEAR: same criterion; no ordering requirement")
    for target in (3, 99):
        print(f"Target {target}:", linear_search(rows, target), "(position, visits)")

    # Pass the key function WITHOUT calling it here: sorted calls it on records.
    # The new list has independent order but shares its record dictionaries.
    # Week 3 used record.copy() for independent earlier values; this is a
    # different ownership choice, not a contradiction. Neither function edits fields.
    ordered = sorted(rows, key=id_key)
    print("\n3. BINARY: same criterion/result contract; ascending ID order")
    print("Search-view IDs:", [id_key(row) for row in ordered])
    for target in (3, 99):
        # Unpack two returned results. position belongs to ordered, not rows.
        position, trace = binary_search(ordered, target)
        print(f"Target {target}: position={position}; (low, high, middle, value)")
        for step in trace:
            print(" ", step)
    print("ID 3 is position 0 in the input, but position 2 in the search view.")

    print("\n4. PRECONDITION: matching alone cannot justify discarding half")
    # Deliberate misuse, not a second valid implementation. Here target 3 is
    # present, but the unsorted midpoint decisions discard the part containing it.
    print("Binary on [3, 1, 2], target 3:", binary_search(rows, 3),
          "<- deliberate precondition violation")
    models = [{"id": 10, "model": "Laptop"}, {"id": 20, "model": "Laptop"},
              {"id": 30, "model": "Tablet"}]
    print("Changed key: model_key, target Laptop; models are already ascending.")
    # The same traversal accepts another named key. Linear returns the first
    # Laptop; binary can return a different Laptop under the any-match contract.
    print("Linear:", linear_search(models, "Laptop", key=model_key))
    print("Binary:", binary_search(models, "Laptop", key=model_key))
    print("IDs are unique; model names can repeat. Search contract permits any matching position.")
    print("An arbitrary filter predicate is not an ordered binary-search comparison.")


if __name__ == "__main__":
    main()
