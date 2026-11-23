"""Help a listener shortlist songs and see how preferences change the order."""

import argparse
from song_data import SONGS
from song_support import validate_weights, require_limit, tags_for
from song_display import show_results, show_ties
from console_style import print_color


def filter_songs(songs, required_tag=None):
    """Return songs containing the optional exact tag without changing the profile."""
    selected = []
    for song in songs:
        tags = tags_for(song)
        if required_tag is None or required_tag in tags:
            selected.append(song)
    return selected


def weighted_similarity(tags, profile, weights):
    """Return matched weight / union weight, contributions, and union weight."""
    validate_weights(weights)
    song_tags = set(tags)
    profile_tags = set(profile)
    matched = song_tags & profile_tags
    union = song_tags | profile_tags
    contributions = {}
    numerator = 0
    for tag in sorted(matched):
        weight = weights.get(tag, 1)
        contributions[tag] = weight
        numerator += weight
    denominator = 0
    for tag in sorted(union):
        denominator += weights.get(tag, 1)
    if denominator == 0:
        score = 0.0
    else:
        score = numerator / denominator
    return score, contributions, denominator


def ranking_key(result):
    """Sort higher scores first and use ascending ID when scores tie."""
    return -result["score"], result["id"]


def rank_songs(songs, profile, weights, k=3):
    """Score every candidate, sort deterministically, and return at most k results."""
    require_limit(k)
    validate_weights(weights)
    scored = []
    for song in songs:
        tags = tags_for(song)
        score, contributions, denominator = weighted_similarity(tags, profile, weights)
        result = {
            "id": song["id"],
            "title": song.get("title", song["id"]),
            "score": score,
            "contributions": contributions,
            "union_weight": denominator,
        }
        scored.append(result)
    ordered = sorted(scored, key=ranking_key)
    return ordered[:k]


def main():
    """Compare ordinary and weighted shortlists after the same optional filter."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emphasis", choices=["calm", "piano"], default="calm")
    parser.add_argument("--tag", help="include only songs with this exact tag")
    parser.add_argument(
        "--limit", type=int, default=3, help="maximum results per list (default: 3)"
    )
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be zero or greater")
    profile = {"calm", "piano"}
    candidates = filter_songs(SONGS, args.tag)
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
    if args.tag is None:
        print(f"Searching all {len(SONGS)} songs.")
    else:
        print(
            f"Tag filter: {args.tag} | {len(candidates)} of {len(SONGS)} songs match."
        )
    print(f"Show up to {args.limit} recommendations in each list.")
    print("Filtering chooses candidates; your preference profile stays calm, piano.")
    baseline = rank_songs(candidates, profile, {}, len(candidates))
    show_results("Equal importance for each tag", baseline, args.limit)
    weights = {args.emphasis: 4}
    weighted = rank_songs(candidates, profile, weights, len(candidates))
    show_results(
        f"Give {args.emphasis} extra importance (weight 4)", weighted, args.limit
    )
    show_ties(weighted, args.limit)
    print("\nScore = matched tag weight / all distinct tag weight.")
    print("Other tags have weight 1; an empty or zero-weight union scores 0.")
    print(
        "These suggestions use fictional tags, not listening history or model training."
    )


if __name__ == "__main__":
    main()
