"""Separate regression checks for both versions of the similarity demo."""

from copy import deepcopy
from math import isclose
import main
import main2


def self_check(module):
    """Check hand-derived scores, empty cases, ordering, and unchanged input."""
    songs = module.SONGS
    original = deepcopy(songs)
    profile = {"calm", "piano"}
    assert module.shared_count(["calm", "calm"], ["calm"]) == 1
    assert module.jaccard(profile, profile) == 1
    assert isclose(module.jaccard({"calm", "acoustic"}, profile), 1 / 3)
    assert module.jaccard([], []) == 0
    assert module.jaccard(["piano"], []) == 0
    assert module.jaccard(["calm", "calm"], ["calm"]) == 1
    scored = module.score_songs(songs, profile)
    assert scored[0]["count"] == scored[4]["count"] == 2
    assert scored[0]["jaccard"] == 1
    assert isclose(scored[4]["jaccard"], 1 / 3)
    assert scored[4]["union_count"] == 6
    assert scored[2]["jaccard"] == 0.5
    assert scored[3]["count"] == scored[3]["jaccard"] == 0
    assert scored[0]["matched"] == ["calm", "piano"]
    count_order = sorted(scored, key=module.count_key)
    similarity_order = sorted(scored, key=module.similarity_key)
    assert [row["id"] for row in count_order] == ["S01", "S05", "S02", "S03", "S04"]
    assert [row["id"] for row in similarity_order] == ["S01", "S03", "S02", "S05", "S04"]
    assert sorted(list(reversed(scored)), key=module.similarity_key) == similarity_order
    missing = [{"id": "M", "title": "No tags"}]
    assert module.score_songs(missing, profile)[0]["jaccard"] == 0
    assert module.score_songs([], profile) == []
    assert module.score_songs(missing, [])[0]["union_count"] == 0
    assert songs == original
    assert profile == {"calm", "piano"}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check(main)
    self_check(main2)
    print("Checks passed for main.py and main2.py.")
