"""Compare two ways to find music for a quiet study session."""

from song_data import SONGS
from song_support import tags_for
from song_display import show_scores, show_order
from console_style import print_color


def shared_count(left, right):
    """Count distinct tags shared by the two collections."""
    left_tags = set(left)
    right_tags = set(right)
    matched = left_tags & right_tags
    return len(matched)


def jaccard(left, right):
    """Return shared tags / all distinct tags, using zero for an empty union."""
    left_tags = set(left)
    right_tags = set(right)
    matched = left_tags & right_tags
    union = left_tags | right_tags
    if not union:
        return 0.0
    return len(matched) / len(union)


def score_songs(songs, profile):
    """Build named results explaining each song's overlap and Jaccard score."""
    scored = []
    profile_tags = set(profile)
    for song in songs:
        tags = tags_for(song)
        matched = tags & profile_tags
        union = tags | profile_tags
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
    return -result["count"], result["id"]


def similarity_key(result):
    """Put larger Jaccard scores first, with ascending ID for ties."""
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
    count_order = sorted(scored, key=count_key)
    similarity_order = sorted(scored, key=similarity_key)
    show_order("By number of shared tags", count_order)
    show_order("By Jaccard similarity", similarity_order)
    show_scores(scored)
    print_color("\nWhy does Broad Mix move down?", "caution")
    print("Quiet Keys and Broad Mix both share your two preference tags.")
    print("Quiet Keys: 2 shared / 2 distinct = 1.000")
    print("Broad Mix:  2 shared / 6 distinct = 0.333")
    print("Extra tags reduce the normalized match, even when overlap stays the same.")
    print("\nUnknown Track has no supplied tags, so its score is 0.")
    print("Tags describe a possible fit; they do not prove what you will enjoy.")


if __name__ == "__main__":
    main()
