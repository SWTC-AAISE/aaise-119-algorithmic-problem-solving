"""Annotated equivalent of main.py, with the same behavior and output.
Read the short version first; use these comments to explain the lecture concepts."""

from song_data import SONGS
from song_support import tags_for
from song_display import show_scores, show_order
from console_style import print_color


def shared_count(left, right):
    """Count distinct tags shared by the two collections."""
    # Convert each collection separately; duplicate tags count only once.
    left_tags = set(left)
    right_tags = set(right)
    # The & operator is set intersection: tags present on BOTH sides.
    matched = left_tags & right_tags
    return len(matched)


def jaccard(left, right):
    """Return shared tags / all distinct tags, using zero for an empty union."""
    # Convert each collection separately; duplicate tags count only once.
    left_tags = set(left)
    right_tags = set(right)
    # The & operator is set intersection: tags present on BOTH sides.
    matched = left_tags & right_tags
    # The | operator is set union: every distinct tag present on EITHER side.
    union = left_tags | right_tags
    # Our empty-union convention is 0; avoid dividing by zero.
    if not union:
        return 0.0
    # Normalization compares the overlap with the size of the combined set.
    # A song with many unrelated tags can keep its raw count but lose similarity.
    return len(matched) / len(union)


def score_songs(songs, profile):
    """Build named results explaining each song's overlap and Jaccard score."""
    scored = []
    # Convert the profile once before comparing each song.
    profile_tags = set(profile)
    for song in songs:
        # This supplied helper makes missing/None tags an empty set.
        tags = tags_for(song)
        matched = tags & profile_tags
        union = tags | profile_tags
        # Named fields keep the score and its explanation readable together.
        # The source song is unchanged; this is a new result dictionary.
        result = {
            "id": song["id"],
            "title": song["title"],
            "count": shared_count(tags, profile_tags),
            "jaccard": jaccard(tags, profile_tags),
            "matched": sorted(matched),
            "union_count": len(union),
        }
        scored.append(result)
    return scored


def count_key(result):
    """Put larger overlap counts first, with ascending ID for ties."""
    # Supplied display ordering: higher counts first, then ID for equal counts.
    # Negative values allow a normal ascending sort to put larger counts first.
    return -result["count"], result["id"]


def similarity_key(result):
    """Put larger Jaccard scores first, with ascending ID for ties."""
    # Use the same tie policy for a fair comparison of the two scoring rules.
    return -result["jaccard"], result["id"]


def main():
    """Show useful recommendations, then explain why the two orders differ."""
    print_color(
        "\n===================================================================",
        "heading",
    )
    print_color("FIND MUSIC FOR A QUIET STUDY SESSION", "heading")
    print_color(
        "===================================================================\n",
        "heading",
    )
    print("Your preferences: calm, piano")
    print("Compare five songs using their fictional tags.\n")
    scored = score_songs(SONGS, {"calm", "piano"})
    # Both views use the SAME scores and source data, ordered by different rules.
    # These helpers arrange the display; Tuesday teaches ranking/top-k in detail.
    count_order = sorted(scored, key=count_key)
    similarity_order = sorted(scored, key=similarity_key)
    show_order("By number of shared tags", count_order)
    show_order("By Jaccard similarity", similarity_order)
    # The small arithmetic table intentionally explains the algorithm.
    # Useful song names appear first, before technical scoring detail.
    show_scores(scored)
    print_color("\nWhy does Broad Mix move down?", "caution")
    print("Quiet Keys and Broad Mix both share your two preference tags.")
    # Pause for a prediction: both songs have count 2, so why does the order change?
    print("Quiet Keys: 2 shared / 2 distinct = 1.000")
    print("Broad Mix:  2 shared / 6 distinct = 0.333")
    print("Extra tags reduce the normalized match, even when overlap stays the same.")
    print("\nUnknown Track has no supplied tags, so its score is 0.")
    print("Tags describe a possible fit; they do not prove what you will enjoy.")


if __name__ == "__main__":
    main()
