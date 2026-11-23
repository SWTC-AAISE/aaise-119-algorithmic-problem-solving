"""Supplied console presentation; scoring and ranking stay in student main.py."""

from console_style import print_color


def show_baseline(rows):
    """Show the Monday score comparison using names and matched features."""
    print_color("\nTopic matches before ranking", "heading")
    for row in rows:
        print(f"{row['title']} ({row['id']})")
        print(f"  Shared tags: {row['count']} | Jaccard: {row['score']:.3f}")
        matched = ", ".join(row["matched"])
        if not matched:
            matched = "none"
        print("  Matching topics: " + matched)


def show_ranking(title, rows, total, limit):
    """Present at most k recommendations and their weighted explanations."""
    print_color("\n" + title, "heading")
    print(f"Showing {len(rows)} of {total} resources; maximum {limit}.")
    if not rows:
        print("No recommendations displayed for this request.")
    for place, row in enumerate(rows, 1):
        print(f"{place}. {row['title']} ({row['id']}) | Score: {row['score']:.3f}")
        print("   " + row["url"])
        parts = []
        matched_weight = 0
        for tag, weight in row["contributions"].items():
            parts.append(f"{tag} ({weight})")
            matched_weight += weight
        if parts:
            print("   Matching topics: " + ", ".join(parts))
        else:
            print("   No matching profile topics.")
        print(f"   Matched weight: {matched_weight}; union weight: {row['union_weight']}")


def same_recommendations(before, after):
    """Compare only IDs and scores, since names and URLs are presentation fields."""
    if len(before) != len(after):
        return False
    for index in range(len(before)):
        if before[index]["id"] != after[index]["id"]:
            return False
        if before[index]["score"] != after[index]["score"]:
            return False
    return True


def show_change(label, unchanged):
    """State whether a selected outcome stayed the same."""
    if unchanged:
        print_color(label + ": UNCHANGED", "success")
    else:
        print_color(label + ": CHANGED", "caution")


def show_digest_pair(original, edited):
    """Present the result first and full digest values as labeled technical evidence."""
    show_change("Metadata fingerprint", original == edited)
    print("Technical evidence - SHA-256 of the selected metadata:")
    print("Original:   " + original)
    print("Title edit: " + edited)
