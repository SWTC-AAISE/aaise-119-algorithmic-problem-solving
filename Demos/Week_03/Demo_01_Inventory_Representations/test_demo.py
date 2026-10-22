"""Regression checks, separate from the classroom application."""

from main import (
    available_ids,
    build_index,
    fixture,
    scan_lookup,
)


def self_check():
    """Check lookup, copied records, availability filtering, and duplicate policy."""
    rows = fixture()
    index = build_index(rows)
    assert scan_lookup(rows, "E03") == (rows[2], 3)
    assert index.get("missing") is None
    index["E01"]["available"] = False
    assert rows[0]["available"] is True
    assert available_ids(index) == ["E02"]
    assert available_ids({}) == []
    assert index["E01"]["available"] is False
    assert scan_lookup(rows, "missing") == (None, 3)
    assert scan_lookup([], "missing") == (None, 0)
    assert index["E01"] is not rows[0]
    assert available_ids(build_index(rows)) == ["E01", "E02"]

    equipment_types = set()
    for row in rows:
        equipment_types.add(row["type"])
    assert equipment_types == {row["type"] for row in rows}
    assert equipment_types == {"laptop", "tablet"}
    equipment_types.add("laptop")
    assert len(equipment_types) == 2
    equipment_types.discard("camera")
    assert len(equipment_types) == 2

    duplicate_rows = rows.copy()
    duplicate_rows.append(rows[0].copy())
    try:
        build_index(duplicate_rows)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate IDs must be rejected")
    assert build_index([]) == {}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
