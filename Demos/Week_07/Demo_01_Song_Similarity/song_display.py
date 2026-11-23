"""Readable song recommendations and a purposeful small score comparison."""

from console_style import print_color


def show_order(title, ordered):
    """Display an ordered list using song names rather than raw ID arrays."""
    print_color(title, "heading")
    for place, result in enumerate(ordered, 1):
        print(f"{place}. {result['title']} ({result['id']})")
    print()


def show_scores(scored):
    """Show the arithmetic behind the recommendations in a labeled table."""
    print_color("How the scores were calculated", "heading")
    print(f"{'Song':<20} {'Shared':>6} {'Distinct':>8} {'Jaccard':>8}  Matching tags")
    print("-" * 76)
    for result in scored:
        matched_text = ", ".join(result["matched"])
        if not matched_text:
            matched_text = "No shared tags"
        print(f"{result['title']:<20} {result['count']:>6} "
              f"{result['union_count']:>8} {result['jaccard']:>8.3f}  {matched_text}")
