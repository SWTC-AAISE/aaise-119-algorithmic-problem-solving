"""Regression checks, separate from the classroom application."""

from main import (
    EQUIPMENT,
    battery_key,
    binary_search,
    filter_available,
    id_key,
    is_eligible,
    linear_search,
    order_for_search,
)


def self_check():
    """Check eligibility, view-relative lookup, ordering, and cross-day contracts."""
    selected = filter_available(EQUIPMENT)
    display = sorted(selected, key=battery_key)
    search_view = order_for_search(selected, key=id_key)
    assert binary_search(display, 3, key=id_key)[0] is None
    assert binary_search(search_view, 3, key=id_key)[0] == 2
    assert linear_search(selected, 3, key=id_key)[0] == 0
    assert isinstance(search_view, list)
    assert [id_key(row) for row in search_view] == [1, 2, 3]
    assert order_for_search([]) == []
    assert search_view is not selected
    assert search_view[2] is selected[0]
    assert [id_key(row) for row in filter_available(EQUIPMENT, 80)] == [1, 2]
    assert filter_available(EQUIPMENT, 100) == []
    assert not is_eligible(EQUIPMENT[3])
    assert binary_search([], 1) == (None, [])
    assert linear_search([], 1) == (None, [])
    assert [id_key(row) for row in EQUIPMENT] == [3, 1, 2, 4]
    for target in (1, 2, 3, 4, 99):
        scan_position, _ = linear_search(selected, target, key=id_key)
        binary_position, _ = binary_search(search_view, target, key=id_key)
        scanned = selected[scan_position] if scan_position is not None else None
        found = search_view[binary_position] if binary_position is not None else None
        assert scanned == found
    battery_view = order_for_search(selected, key=battery_key)
    for target in (20, 80, 90, 70):
        scan_position, _ = linear_search(selected, target, key=battery_key)
        binary_position, _ = binary_search(battery_view, target, key=battery_key)
        scanned = selected[scan_position] if scan_position is not None else None
        found = battery_view[binary_position] if binary_position is not None else None
        assert scanned == found
    changed = filter_available(EQUIPMENT, 80)
    changed_view = order_for_search(changed)
    assert linear_search(changed, 3)[0] is None
    assert binary_search(changed_view, 3)[0] is None
    assert binary_search([EQUIPMENT[0]], 3)[0] == 0
    # A new ordered list shares records, but preserves the source list's order.
    local_records = [record.copy() for record in EQUIPMENT]
    before = [record.copy() for record in local_records]
    local_view = order_for_search(local_records)
    assert local_records == before
    local_records[0]["battery"] = 25
    assert local_view[2]["battery"] == 25
    assert EQUIPMENT[0]["battery"] == 20
    # Tied-key library ordering remains stable without comparator instrumentation.
    tied = [{"id": "A", "battery": 70}, {"id": "B", "battery": 50},
            {"id": "C", "battery": 70}]
    assert [row["id"] for row in order_for_search(tied, battery_key)] == ["B", "A", "C"]


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
