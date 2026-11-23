"""Annotated equivalent of main.py, with the same behavior and output.
Read the short version first; use these comments to explain the lecture concepts."""

from copy import deepcopy
import hashlib
from playlist_data import PLAYLIST
from snapshot_support import canonical_bytes, tags_for
from playlist_display import show_ranking, show_digest_comparison
from console_style import print_color


def digest(playlist):
    """Return the SHA-256 fingerprint of our consistently serialized metadata."""
    # Use the supplied serialization contract: consistent fields, ordering and bytes.
    # The helper is support code, not a cryptographic algorithm to implement.
    snapshot = canonical_bytes(playlist)
    # Give the bytes to the standard library; no audio data is being hashed.
    fingerprint = hashlib.sha256(snapshot)
    # Hexadecimal is a printable form of the digest, not encrypted playlist data.
    return fingerprint.hexdigest()


def ranking_key(result):
    """Order higher scores first and use ascending ID for equal scores."""
    # Reuse Tuesday's deterministic score-first, ID-second ordering rule.
    return -result["score"], result["id"]


def rank(playlist, profile):
    """Return IDs and Jaccard scores, independently of song titles."""
    scores = []
    # Reuse Monday's Jaccard calculation so a new scoring rule adds no distraction.
    profile_tags = set(profile)
    for song in playlist:
        tags = tags_for(song)
        matched = tags & profile_tags
        union = tags | profile_tags
        # Our policy for an empty union is still zero.
        if not union:
            score = 0.0
        else:
            score = len(matched) / len(union)
        # These results deliberately omit titles: titles do not affect tag matching.
        # The display gets names from whichever snapshot it is showing.
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
    # Keep the original result as a reference for both independent scenarios.
    baseline = rank(PLAYLIST, {"calm", "piano"})
    show_ranking("Original suggestions", PLAYLIST, baseline)

    # A playlist contains dictionaries that contain tag lists.
    # deepcopy gives this scenario independent nested data.
    # Copying only the outer list would still share the inner dictionaries.
    missing = deepcopy(PLAYLIST)
    # Erase metadata in the copy only; the song itself did not change.
    # A lower score can reflect missing information, not a worse musical fit.
    missing[0]["tags"] = []
    changed_ranking = rank(missing, {"calm", "piano"})
    show_ranking("After Quiet Keys loses its tags", missing, changed_ranking)
    print("The top suggestion changed even though the music did not.")
    print("Missing information can hide a good match.")

    # This original is a trusted local reference for our controlled demonstration.
    # A real comparison also needs a trustworthy reference value.
    original_digest = digest(PLAYLIST)
    # Start again from the ORIGINAL, not from the missing-tags scenario.
    # This isolates the effect of one title change.
    renamed = deepcopy(PLAYLIST)
    renamed[0]["title"] = "Quiet Keys (edited title)"
    renamed_digest = digest(renamed)
    renamed_ranking = rank(renamed, {"calm", "piano"})
    show_ranking(
        "After a title-only edit to the original playlist", renamed, renamed_ranking
    )
    # The ID/score records stay equal because tags and preferences are unchanged.
    if renamed_ranking == baseline:
        print_color("Recommendation order and scores: UNCHANGED", "success")
    else:
        print_color("Recommendation order or scores: CHANGED", "caution")
    # The serialization contract includes titles, so the digest should change.
    # A change detector and a recommendation score answer different questions.
    show_digest_comparison(original_digest, renamed_digest)
    print("\nThe fingerprint includes IDs, titles, and unique sorted tags.")
    print("It checks this metadata snapshot, not the audio or recommendation quality.")
    print("A match alone does not prove authenticity, fairness, or source accuracy.")
    print("This fingerprint is not Python's lookup hash() or encryption.")


if __name__ == "__main__":
    main()
