"""Regression checks, separate from the classroom application."""

from main import (
    EQUIPMENT,
    ready_for_loan,
    matches_laptop_request,
    ids,
    original_selection,
    select_equipment,
)


def self_check():
    """Verify refactor parity, changed requirements, and input preservation."""
    assert ids(original_selection(EQUIPMENT)) == ["E01", "E02", "E04"]
    assert select_equipment(EQUIPMENT, ready_for_loan) == original_selection(EQUIPMENT)
    assert ids(select_equipment(EQUIPMENT, matches_laptop_request)) == ["E01", "E04"]
    assert select_equipment([], matches_laptop_request) == []
    assert select_equipment(EQUIPMENT[1:3], matches_laptop_request) == []
    assert not ready_for_loan({"id": "X", "type": "laptop", "available": True, "battery": True})
    before = [record.copy() for record in EQUIPMENT]
    result = select_equipment(EQUIPMENT, matches_laptop_request)
    result[0]["battery"] = 0
    assert EQUIPMENT == before


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
