"""Regression checks, separate from the classroom application."""

from main import (
    checkout_next,
    enqueue,
    make_state,
    undo_checkout,
)


def self_check():
    """Check request order, named undo data, invalid requests, and full restoration."""
    state = make_state()
    assert checkout_next(state) == "queue empty"
    assert undo_checkout(state) == "nothing to undo"
    enqueue(state, "E01")
    enqueue(state, "E02")
    checkout_next(state)
    assert state["inventory"]["E01"] is False
    assert list(state["pending"]) == ["E02"]
    assert state["undo"] == [{"equipment_id": "E01", "previous_available": True}]
    undo_checkout(state)
    assert state["inventory"]["E01"] is True
    assert list(state["pending"]) == ["E01", "E02"]
    assert state["undo"] == []
    checkout_next(state)
    checkout_next(state)
    undo_checkout(state)
    assert list(state["pending"]) == ["E02"]
    assert state["inventory"]["E01"] is False
    assert state["inventory"]["E02"] is True
    assert state["undo"] == [{"equipment_id": "E01", "previous_available": True}]
    undo_checkout(state)
    assert list(state["pending"]) == ["E01", "E02"]
    assert state["inventory"] == {"E01": True, "E02": True}
    assert state["undo"] == []

    for invalid_id in ("missing", "E01"):
        try:
            enqueue(state, invalid_id)
        except ValueError:
            pass
        else:
            raise AssertionError("unknown IDs and duplicate requests must be rejected")
    assert list(state["pending"]) == ["E01", "E02"]

    denied = make_state()
    denied["inventory"]["E01"] = False
    enqueue(denied, "E01")
    assert checkout_next(denied) == "E01: denied (unavailable); request consumed"
    assert list(denied["pending"]) == []
    assert denied["undo"] == []
    assert denied["inventory"]["E01"] is False


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
