"""Separate regression checks for metadata integrity and recommendation limits."""

from copy import deepcopy
import main
import main2


def self_check(module):
    """Check digest reproducibility, isolated edits, and declared field boundaries."""
    playlist = module.PLAYLIST
    original = deepcopy(playlist)
    profile = {"calm", "piano"}
    baseline = module.rank(playlist, profile)
    assert baseline == [{"id": "S01", "score": 1.0}, {"id": "S02", "score": 1 / 3}]
    assert module.digest(playlist) == "de39dbcc9fa4dd2ca5761048751667ec9e17870aa6b5b3574cd021c4a0ea3d7f"
    reordered = deepcopy(list(reversed(playlist)))
    for song in reordered:
        song["tags"].reverse()
    assert module.digest(reordered) == module.digest(playlist)
    renamed = deepcopy(playlist)
    renamed[0]["title"] = "Renamed"
    assert module.digest(renamed) != module.digest(playlist)
    assert module.rank(renamed, profile) == baseline
    missing = deepcopy(playlist)
    missing[0]["tags"] = []
    assert module.rank(missing, profile) == [
        {"id": "S02", "score": 1 / 3}, {"id": "S01", "score": 0},
    ]
    assert module.digest(missing) != module.digest(playlist)
    duplicates = deepcopy(playlist)
    duplicates[0]["tags"].append("calm")
    assert module.digest(duplicates) == module.digest(playlist)
    assert module.rank(duplicates, profile) == baseline
    extra = deepcopy(playlist)
    extra[0]["unselected_field"] = "Not part of our snapshot contract"
    assert module.digest(extra) == module.digest(playlist)
    assert module.rank([], profile) == []
    assert len(module.digest([])) == 64
    absent = [{"id": "X", "title": "Missing tags"}]
    explicit_none = [{"id": "X", "title": "Missing tags", "tags": None}]
    empty_tags = [{"id": "X", "title": "Missing tags", "tags": []}]
    assert module.digest(absent) == module.digest(explicit_none) == module.digest(empty_tags)
    assert module.rank(absent, []) == [{"id": "X", "score": 0}]
    ties = [
        {"id": "B", "title": "First in data", "tags": ["calm"]},
        {"id": "A", "title": "Second in data", "tags": ["calm"]},
    ]
    assert module.rank(ties, ["calm"]) == [
        {"id": "A", "score": 1}, {"id": "B", "score": 1},
    ]
    try:
        module.digest(playlist + [deepcopy(playlist[0])])
    except ValueError as error:
        assert "duplicate" in str(error)
    else:
        raise AssertionError("duplicate IDs accepted")
    assert playlist == original
    assert profile == {"calm", "piano"}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check(main)
    self_check(main2)
    print("Checks passed for main.py and main2.py.")
