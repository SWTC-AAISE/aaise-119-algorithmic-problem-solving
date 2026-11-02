"""Separate matching criteria from traversal and then introduce ordered search."""


def id_key(record):
    """Select the equipment ID without searching or changing the record."""
    return record["id"]


def matches(value, target):
    """Equality is the same rule for both search strategies."""
    return value == target


def compare_values(value, target):
    """Ordered, comparable values: negative, zero, or positive."""
    if matches(value, target):
        return 0
    return -1 if value < target else 1


def linear_search(records, target, key=id_key):
    """Return a position in this view and a visit trace; None means absent."""
    trace = []
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace


def binary_search(records, target, key=id_key):
    """Same result contract; requires ascending order under this exact key."""
    # Initialize local variables - using "packed" style
    low, high, trace = 0, len(records) - 1, []

    while low <= high:
        middle = (low + high) // 2
        value = key(records[middle])
        trace.append((low, high, middle, value))
        comparison = compare_values(value, target)
        if comparison == 0:
            return middle, trace
        if comparison < 0:
            low = middle + 1
        else:
            high = middle - 1
    return None, trace


def model_key(record):
    """Select the model name as an alternative search key."""
    return record["model"]


def fixture():
    """Provide three records deliberately outside ascending ID order."""
    return [
        {"id": 3, "battery": 20},
        {"id": 1, "battery": 80},
        {"id": 2, "battery": 90},
    ]


def main():
    """Demonstrate shared search contracts and deliberate precondition failures."""
    rows = fixture()
    print(
        "SEARCH SCAFFOLD: key -> match -> linear traversal -> ordered binary traversal"
    )
    print("Shared contract: (position in supplied view, trace); None means absent")

    print("\n1. CRITERIA: id_key selects a value; matches defines equality")
    print("Input IDs:", [id_key(row) for row in rows])
    print("First record matches ID 3:", matches(id_key(rows[0]), 3))
    print("First record matches ID 99:", matches(id_key(rows[0]), 99))

    print("\n2. LINEAR: same criterion; no ordering requirement")
    for target in (3, 99):
        print(f"Target {target}:", linear_search(rows, target), "(position, visits)")

    ordered = sorted(rows, key=id_key)
    print("\n3. BINARY: same criterion/result contract; ascending ID order")
    print("Search-view IDs:", [id_key(row) for row in ordered])
    for target in (3, 99):
        position, trace = binary_search(ordered, target)
        print(f"Target {target}: position={position}; (low, high, middle, value)")
        for step in trace:
            print(" ", step)
    print("ID 3 is position 0 in the input, but position 2 in the search view.")

    print("\n4. PRECONDITION: matching alone cannot justify discarding half")
    print(
        "Binary on [3, 1, 2], target 3:",
        binary_search(rows, 3),
        "<- deliberate precondition violation",
    )
    models = [
        {"id": 10, "model": "Laptop"},
        {"id": 20, "model": "Laptop"},
        {"id": 30, "model": "Tablet"},
    ]
    print("Changed key: model_key, target Laptop; models are already ascending.")
    print("Linear:", linear_search(models, "Laptop", key=model_key))
    print("Binary:", binary_search(models, "Laptop", key=model_key))
    print(
        "IDs are unique; model names can repeat. Search contract permits any matching position."
    )
    print("An arbitrary filter predicate is not an ordered binary-search comparison.")


if __name__ == "__main__":
    main()
