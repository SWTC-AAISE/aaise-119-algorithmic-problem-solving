"""Readable playlist suggestions and clearly labeled snapshot evidence."""

from console_style import print_color


def show_ranking(title, playlist, ordered):
    """Display names from this snapshot alongside their ranking scores."""
    print_color("\n" + title, "heading")
    titles = {}
    for song in playlist:
        titles[song["id"]] = song["title"]
    for place, result in enumerate(ordered, 1):
        print(f"{place}. {titles[result['id']]} ({result['id']}) | Score: {result['score']:.3f}")
    if not ordered:
        print("There are no songs to recommend.")


def show_digest_comparison(original, edited):
    """Present a clear change result before the full digest evidence."""
    print_color("\nSaved playlist fingerprint", "heading")
    if original == edited:
        print_color("Metadata fingerprint: UNCHANGED", "success")
    else:
        print_color("Metadata fingerprint: CHANGED", "caution")
    print("Technical evidence - SHA-256 of the metadata snapshot:")
    print("Original:   " + original)
    print("Title edit: " + edited)
