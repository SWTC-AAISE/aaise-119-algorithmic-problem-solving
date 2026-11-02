"""Documented companion to main.py; both versions use the same simplified pipeline.

Thursday combines eligibility, separate views, and Monday's search contracts.
Sorting uses an ordinary named key, without a nested comparator or nonlocal
counter. Generator expressions remain explained as a compact way to total the
small visit traces; separate handouts give explicit-loop equivalents.
"""


def id_key(record):
    """Select the equipment ID without deciding eligibility or traversing data."""
    return record["id"]


def matches(value, target):
    """Apply the same equality decision used by Monday's searches."""
    return value == target


def compare_values(value, target):
    """Return zero for equality, negative one for smaller, or positive one for larger."""
    if matches(value, target):
        return 0
    # Compact conditional expression; ordinary if/else could express the same rule.
    return -1 if value < target else 1


def linear_search(records, target, key=id_key):
    """Return a view-relative position and trace, or None with the visit trace."""
    trace = []
    # enumerate supplies the position and record. key is a callable selector,
    # not a key-name string and not an arbitrary eligibility predicate.
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace


def binary_search(records, target, key=id_key):
    """Use Monday's result contract, assuming ascending order under this exact key."""
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
    # Position zero is a valid result; None means absent. Resolve a returned
    # position against THIS input view, not another differently ordered list.
    return None, trace


EQUIPMENT = [{"id": 3, "battery": 20, "available": True},
             {"id": 1, "battery": 80, "available": True},
             {"id": 2, "battery": 90, "available": True},
             {"id": 4, "battery": 70, "available": False}]


def battery_key(record):
    """Select the battery value for display ordering and eligibility."""
    return record["battery"]


def is_eligible(record, minimum_battery=0):
    """Require both availability and battery at or above the inclusive threshold."""
    # and short-circuits: an unavailable item fails before the battery comparison.
    # This yes/no rule cannot tell binary search which ordered half to discard.
    return record["available"] and battery_key(record) >= minimum_battery


def filter_available(records, minimum_battery=0):
    """Return a separate selected list whose record dictionaries remain shared."""
    # List comprehension: visit records, keep each eligible record reference.
    # No record.copy() is called. A new outer list is NOT an independent snapshot.
    # Week 3 preserved earlier values with flat copies; this view serves another job.
    return [record for record in records if is_eligible(record, minimum_battery)]


def order_for_search(records, key=id_key):
    """Return a new key-ordered list that shares the supplied record dictionaries."""
    # key is a one-record selector, such as id_key or battery_key. sorted calls
    # it for each record; we do not need a two-record comparison adapter/counter.
    # This helper now returns ONE list, not a (list, comparison-count) pair.
    return sorted(records, key=key)


def main():
    """Show separate query views, current count reporting, and a rebuilt selection."""
    print("QUERY PIPELINE: eligibility predicate -> views -> familiar search -> report")
    print("Reused search contract: (position in supplied view, trace); callable key")
    selected = filter_available(EQUIPMENT)
    print("Eligible IDs:", [id_key(row) for row in selected])
    # Display order answers a presentation question. ID lookup requires its own
    # ID-ordered view, not the battery-ordered view, even with the same records.
    display = sorted(selected, key=battery_key)
    search_view = order_for_search(selected, key=id_key)
    # These lists have separate membership/order containers but share records.
    # Reordering one list does not rearrange another. A shared record field edit
    # IS visible through each reference, but does not automatically re-sort or
    # re-filter a view. Treat records as read-only during a run; rebuild affected
    # views from the authoritative source after relevant criteria/data changes.
    print("Battery-ordered display IDs:", [id_key(row) for row in display])
    print("ID-ordered search view:     ", [id_key(row) for row in search_view])
    print("Invalid ID binary search in display, target 3:", binary_search(display, 3)[0])
    # _ marks the trace unused for these two calls. [0] above selects the returned
    # position only; it is not position zero in the equipment inventory.
    linear_position, _ = linear_search(selected, 3)
    binary_position, _ = binary_search(search_view, 3)
    print(f"Same ID 3: linear position={linear_position}; binary position={binary_position}")
    # Fixture ID 3 exists in both views. General lookup callers must check for
    # None before using a result as an index; this is not generic missing-ID code.
    print("Resolve positions against their own views:", selected[linear_position] == search_view[binary_position])
    print("Correct search view, target 3:", search_view[binary_position])
    for count in (1, 12):
        # Conditional expression selects one query or a repeated query list.
        # List * 4 repeats the three ID values; it does not multiply each ID.
        queries = [3, 99, 1] * 4 if count == 12 else [3]
        # Each generator performs searches and yields one trace length at a time.
        # [1] means the trace component; len counts visits; sum totals the visits.
        # The generators handout separates these steps and shows a simple loop.
        scan_work = sum(len(linear_search(selected, target)[1]) for target in queries)
        query_work = sum(len(binary_search(search_view, target)[1]) for target in queries)
        print(f"q={count}: scan inspections={scan_work}; "
              f"binary midpoint inspections={query_work}")
    print("Filter scans 4 input records once; both workflows share that cost.")
    print("The ID search view is ordered once and reused; rebuilding it adds setup work.")
    print("Counts describe search visits, not equal-duration units or total timings.")
    # The selected list shares records, unlike Week 3's independent saved copies.
    print("Traces allocate memory for teaching; both workflows reuse one filtered view.")
    # Rebuild from the original source. Filtering an old selection could miss
    # records newly admitted by a later, less restrictive rule.
    changed = filter_available(EQUIPMENT, 80)
    changed_view = order_for_search(changed, key=id_key)
    print("Changed battery threshold >=80:", [id_key(row) for row in changed])
    print("ID 3 after the filter change:", binary_search(changed_view, 3)[0])
    print("Filtering changes eligibility; it does not change the equality or search contract.")


if __name__ == "__main__":
    main()
