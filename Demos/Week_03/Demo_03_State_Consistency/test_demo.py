"""Regression checks, separate from the classroom application."""

from main import (
    deepcopy,
    deque,
    repair_queue,
    stale_ids,
)


def self_check():
    """Check ordered repair, unchanged inputs, aliases, and independent snapshots."""
    inventory = {"E01": {"available": True}, "E02": {"available": True}}
    pending = deque(["E01", "missing", "E02"])
    repaired, removed = repair_queue(inventory, pending)
    assert list(repaired) == ["E01", "E02"]
    assert removed == ["missing"]
    assert list(pending) == ["E01", "missing", "E02"]
    assert not stale_ids(inventory, repaired)
    aliases = []
    for equipment_id in inventory:
        aliases.append(inventory[equipment_id])
    snapshot = deepcopy(aliases)
    inventory["E01"]["available"] = False
    assert snapshot[0]["available"] is True
    assert aliases[0]["available"] is False
    snapshot[0]["available"] = False
    assert snapshot[0] is not inventory["E01"]
    inventory["E01"]["available"] = True
    assert snapshot[0]["available"] is False
    assert repair_queue({}, deque())[1] == []
    all_missing = deque(["missing", "also missing"])
    empty, missing = repair_queue({}, all_missing)
    assert list(empty) == []
    assert missing == ["missing", "also missing"]
    assert list(all_missing) == ["missing", "also missing"]
    assert list(repair_queue(inventory, repaired)[0]) == ["E01", "E02"]
    assert stale_ids(inventory, repaired) == []


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
