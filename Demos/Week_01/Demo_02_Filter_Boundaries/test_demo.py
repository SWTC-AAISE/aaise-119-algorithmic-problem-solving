"""Regression checks, separate from the classroom application."""

from main import (
    CASES,
    buggy_predicate,
    corrected_predicate,
    select_equipment,
    EQUIPMENT,
)


def self_check():
    """Check the repaired boundary, invalid values, and collection behavior."""
    for _, record, expected in CASES:
        assert corrected_predicate(record, 50) is expected
    assert buggy_predicate(CASES[1][1], 50) is False
    assert not corrected_predicate({"available": True, "battery": True}, 50)
    assert list(filter(lambda row: corrected_predicate(row, 50), [])) == []
    assert select_equipment([]) == ([], [])
    selected, excluded = select_equipment(EQUIPMENT)
    assert [record['id'] for record in selected] == ['E02', 'E03']
    assert len(excluded) == 5
    assert select_equipment(EQUIPMENT[:1])[0] == []
    before = [record.copy() for record in EQUIPMENT]
    selected[0]['battery'] = 0
    assert EQUIPMENT == before
    for threshold in (-1, 101, True, '50'):
        try:
            select_equipment([], threshold)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid threshold accepted')


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
