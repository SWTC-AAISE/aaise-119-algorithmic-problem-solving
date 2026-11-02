"""Regression checks, separate from the classroom application."""

from main import (
    binary_search,
    fixture,
    id_key,
    linear_search,
    matches,
    model_key,
)


def self_check():
    """Check shared keys, search results, duplicate policy, and ordering failures."""
    rows = fixture()
    ordered = sorted(rows, key=id_key)
    assert matches(id_key(rows[0]), 3)
    assert not matches(id_key(rows[0]), 99)
    assert [id_key(row) for row in rows] == [3, 1, 2]
    for target in (1, 2, 3, 99):
        linear_position, _ = linear_search(ordered, target)
        binary_position, _ = binary_search(ordered, target)
        assert linear_position == binary_position
    assert linear_search(rows, 3) == (0, [(0, 3)])
    assert binary_search(rows, 3)[0] is None
    for search in (linear_search, binary_search):
        assert search([], 1) == (None, [])
        assert search([{"id": 1}], 1)[0] == 0
        assert search([{"id": 1}], 99)[0] is None
        assert search(ordered, 99)[0] is None
    models = [{"id": 10, "model": "Laptop"}, {"id": 20, "model": "Laptop"},
              {"id": 30, "model": "Tablet"}]
    for search in (linear_search, binary_search):
        position, _ = search(models, "Laptop", key=model_key)
        assert position is not None and model_key(models[position]) == "Laptop"
        assert search(models, "Camera", key=model_key)[0] is None
    assert len({id_key(row) for row in models}) == 3
    display = sorted(rows, key=lambda row: row["battery"])
    assert binary_search(display, 3, key=id_key)[0] is None


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
