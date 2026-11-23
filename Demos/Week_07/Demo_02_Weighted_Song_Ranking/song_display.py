"""Readable shortlists and small, explicitly labeled ranking explanations."""

from console_style import print_color


def show_results(title, ordered, limit):
    """Display a limited list, matching count, and each result's score explanation."""
    print_color("\n" + title, "heading")
    shown = ordered[:limit]
    print(f"Showing {len(shown)} of {len(ordered)} matching songs.")
    if not ordered:
        print("No songs match this filter. Try another tag or leave --tag out.")
        return
    if limit == 0:
        print("The result limit is zero; no recommendations are displayed.")
    for place, result in enumerate(shown, 1):
        print(f"{place}. {result['title']} ({result['id']}) | Score: {result['score']:.3f}")
        parts = []
        matched_weight = 0
        for tag, weight in result["contributions"].items():
            parts.append(f"{tag} ({weight})")
            matched_weight += weight
        if parts:
            print("   Matches: " + ", ".join(parts))
        else:
            print("   No matching preference tags.")
        print(f"   Matched weight: {matched_weight}; all distinct tag weight: {result['union_weight']}")
    hidden = len(ordered) - len(shown)
    if hidden:
        print(f"{hidden} additional matching song(s) are outside the top {limit}.")


def show_ties(ordered, limit):
    """Explain equal scores in the full candidate list, including cutoff ties."""
    if limit == 0:
        return
    for index in range(1, len(ordered)):
        previous = ordered[index - 1]
        current = ordered[index]
        if previous["score"] == current["score"]:
            print_color("\nWhy this order? Equal-score example", "caution")
            print(f"{previous['title']} ({previous['id']}) and {current['title']} ({current['id']})")
            print(f"both score {current['score']:.3f}; the lower ID comes first.")
            if index == limit:
                print(f"Only {previous['id']} fits at the cutoff; {current['id']} is outside this shortlist.")
            print("The ID rule makes the result repeatable; it does not mean one song sounds better.")
            return
