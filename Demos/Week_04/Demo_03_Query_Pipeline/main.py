"""Compose familiar callable-key searches without changing their result contract."""

def id_key(record):
    """Select the ID used by the shared search contract."""
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


EQUIPMENT = [{"id": 3, "battery": 20, "available": True},
             {"id": 1, "battery": 80, "available": True},
             {"id": 2, "battery": 90, "available": True},
             {"id": 4, "battery": 70, "available": False}]


def battery_key(record):
    """Select the battery value used for display ordering and eligibility."""
    return record["battery"]


def is_eligible(record, minimum_battery=0):
    """Accept available equipment meeting the inclusive battery minimum."""
    return record["available"] and battery_key(record) >= minimum_battery


def filter_available(records, minimum_battery=0):
    """Return a new selected list sharing the matching record dictionaries."""
    return [record for record in records if is_eligible(record, minimum_battery)]


def order_for_search(records, key=id_key):
    """Return a new key-ordered list sharing the supplied record dictionaries."""
    return sorted(records, key=key)


def main():
    """Compare valid query views and rebuild them after an eligibility change."""
    print("QUERY PIPELINE: eligibility predicate -> views -> familiar search -> report")
    print("Reused search contract: (position in supplied view, trace); callable key")
    selected = filter_available(EQUIPMENT)
    print("Eligible IDs:", [id_key(row) for row in selected])
    display = sorted(selected, key=battery_key)
    search_view = order_for_search(selected, key=id_key)
    print("Battery-ordered display IDs:", [id_key(row) for row in display])
    print("ID-ordered search view:     ", [id_key(row) for row in search_view])
    print("Invalid ID binary search in display, target 3:", binary_search(display, 3)[0])
    linear_position, _ = linear_search(selected, 3)
    binary_position, _ = binary_search(search_view, 3)
    print(f"Same ID 3: linear position={linear_position}; binary position={binary_position}")
    print("Resolve positions against their own views:", selected[linear_position] == search_view[binary_position])
    print("Correct search view, target 3:", search_view[binary_position])
    for count in (1, 12):
        queries = [3, 99, 1] * 4 if count == 12 else [3]
        scan_work = sum(len(linear_search(selected, target)[1]) for target in queries)
        query_work = sum(len(binary_search(search_view, target)[1]) for target in queries)
        print(f"q={count}: scan inspections={scan_work}; "
              f"binary midpoint inspections={query_work}")
    print("Filter scans 4 input records once; both workflows share that cost.")
    print("The ID search view is ordered once and reused; rebuilding it adds setup work.")
    print("Counts describe search visits, not equal-duration units or total timings.")
    print("Traces allocate memory for teaching; both workflows reuse one filtered view.")
    changed = filter_available(EQUIPMENT, 80)
    changed_view = order_for_search(changed, key=id_key)
    print("Changed battery threshold >=80:", [id_key(row) for row in changed])
    print("ID 3 after the filter change:", binary_search(changed_view, 3)[0])
    print("Filtering changes eligibility; it does not change the equality or search contract.")


if __name__ == "__main__":
    main()
