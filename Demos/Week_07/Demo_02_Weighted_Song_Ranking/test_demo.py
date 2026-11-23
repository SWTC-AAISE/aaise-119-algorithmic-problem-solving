"""Check ranking, filtering, cutoff ties, and both classroom code versions."""

from copy import deepcopy
from math import isclose
import main
import main2


def self_check(module):
    """Check independently derived outcomes and preserve the input catalog."""
    songs = module.SONGS
    original = deepcopy(songs)
    profile = {"calm", "piano"}
    baseline = module.rank_songs(songs, profile, {}, 6)
    weighted = module.rank_songs(songs, profile, {"calm": 4}, 6)
    assert [row["id"] for row in baseline] == ["S01", "S06", "S03", "S02", "S05", "S04"]
    assert [row["id"] for row in weighted] == ["S01", "S06", "S02", "S05", "S03", "S04"]
    assert isclose(weighted[2]["score"], 4 / 6)
    assert weighted[2]["contributions"] == {"calm": 4}
    assert weighted[2]["union_weight"] == 6
    assert [row["id"] for row in module.rank_songs(songs, profile, {})] == ["S01", "S06", "S03"]
    assert [row["id"] for row in module.rank_songs(songs, profile, {"calm": 4})] == ["S01", "S06", "S02"]

    candidates = module.filter_songs(songs, "calm")
    assert [song["id"] for song in candidates] == ["S01", "S05", "S02", "S06"]
    ranked = module.rank_songs(candidates, profile, {"calm": 4}, 4)
    assert [row["id"] for row in ranked] == ["S01", "S06", "S02", "S05"]
    assert ranked[2]["score"] == ranked[3]["score"]
    assert [row["id"] for row in module.rank_songs(candidates, profile, {"calm": 4}, 3)] == ["S01", "S06", "S02"]
    assert module.rank_songs(list(reversed(candidates)), profile, {"calm": 4}, 4) == ranked
    assert module.filter_songs(songs, "not-a-tag") == []
    assert module.filter_songs(songs) == songs
    assert module.rank_songs([], profile, {}) == []
    assert module.rank_songs(songs, profile, {}, 0) == []
    assert len(module.rank_songs(songs, profile, {}, 99)) == 6

    score, contributions, denominator = module.weighted_similarity([], [], {})
    assert (score, contributions, denominator) == (0, {}, 0)
    assert module.weighted_similarity(["calm"], ["calm"], {"calm": 0})[0] == 0
    assert module.weighted_similarity(["calm", "calm"], ["calm"], {})[0] == 1
    missing = [{"id": "M"}, {"id": "N", "tags": None}]
    assert module.filter_songs(missing, "calm") == []
    assert [row["score"] for row in module.rank_songs(missing, profile, {})] == [0, 0]

    for invalid in (-1, float("nan"), float("inf"), True, "4"):
        try:
            module.weighted_similarity(["calm"], ["calm"], {"calm": invalid})
        except ValueError:
            pass
        else:
            raise AssertionError("invalid weight accepted")
    for invalid in (-1, True, 1.5):
        try:
            module.rank_songs(songs, profile, {}, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid limit accepted")
    assert songs == original
    assert profile == {"calm", "piano"}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check(main)
    self_check(main2)
    print("Checks passed for main.py and main2.py.")
