"""Check a saved playlist for metadata changes without judging musical quality."""

from copy import deepcopy
import hashlib
from playlist_data import PLAYLIST
from snapshot_support import canonical_bytes, tags_for
from playlist_display import show_ranking, show_digest_comparison
from console_style import print_color


def digest(playlist):
    """Return the SHA-256 fingerprint of our consistently serialized metadata."""
    snapshot = canonical_bytes(playlist)
    fingerprint = hashlib.sha256(snapshot)
    return fingerprint.hexdigest()


def ranking_key(result):
    """Order higher scores first and use ascending ID for equal scores."""
    return -result["score"], result["id"]


def rank(playlist, profile):
    """Return IDs and Jaccard scores, independently of song titles."""
    scores = []
    profile_tags = set(profile)
    for song in playlist:
        tags = tags_for(song)
        matched = tags & profile_tags
        union = tags | profile_tags
        if not union:
            score = 0.0
        else:
            score = len(matched) / len(union)
        scores.append({"id": song["id"], "score": score})
    return sorted(scores, key=ranking_key)


def main():
    """Compare missing-tag and title-only edits against an unchanged original."""
    print_color(
        "\n===================================================================",
        "heading",
    )
    print_color("CHECK A SAVED STUDY PLAYLIST", "heading")
    print_color(
        "===================================================================\n",
        "heading",
    )
    print("Your preferences: calm, piano")
    baseline = rank(PLAYLIST, {"calm", "piano"})
    show_ranking("Original suggestions", PLAYLIST, baseline)

    missing = deepcopy(PLAYLIST)
    missing[0]["tags"] = []
    changed_ranking = rank(missing, {"calm", "piano"})
    show_ranking("After Quiet Keys loses its tags", missing, changed_ranking)
    print("The top suggestion changed even though the music did not.")
    print("Missing information can hide a good match.")

    original_digest = digest(PLAYLIST)
    renamed = deepcopy(PLAYLIST)
    renamed[0]["title"] = "Quiet Keys (edited title)"
    renamed_digest = digest(renamed)
    renamed_ranking = rank(renamed, {"calm", "piano"})
    show_ranking(
        "After a title-only edit to the original playlist", renamed, renamed_ranking
    )
    if renamed_ranking == baseline:
        print_color("Recommendation order and scores: UNCHANGED", "success")
    else:
        print_color("Recommendation order or scores: CHANGED", "caution")
    show_digest_comparison(original_digest, renamed_digest)
    print("\nThe fingerprint includes IDs, titles, and unique sorted tags.")
    print("It checks this metadata snapshot, not the audio or recommendation quality.")
    print("A match alone does not prove authenticity, fairness, or source accuracy.")
    print("This fingerprint is not Python's lookup hash() or encryption.")


if __name__ == "__main__":
    main()
