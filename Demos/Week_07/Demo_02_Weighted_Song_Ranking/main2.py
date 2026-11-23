"""Annotated equivalent of main.py: the same shortlist and algorithm behavior.

Optional compact equivalent for recognition, not executed:
    denominator = sum(weights.get(tag, 1) for tag in union)
AI explanation prompt: Explain this generator expression inside sum(). Compare
it with our explicit accumulator loop, using the same tags and weights.
"""

import argparse
from song_data import SONGS
from song_support import validate_weights, require_limit, tags_for
from song_display import show_results, show_ties
from console_style import print_color


def filter_songs(songs, required_tag=None):
    """Return songs containing the optional exact tag without changing the profile."""
    # The filter only decides which catalog records are eligible.
    # It does not remove tags or change what the listener prefers.
    selected = []
    for song in songs:
        tags = tags_for(song)
        # Without --tag, keep every song. With it, require an exact tag match.
        if required_tag is None or required_tag in tags:
            selected.append(song)
    return selected


def weighted_similarity(tags, profile, weights):
    """Return matched weight / union weight, contributions, and union weight."""
    validate_weights(weights)
    # Sets remove duplicate tags so repeated words do not inflate a score.
    song_tags = set(tags)
    profile_tags = set(profile)
    # Intersection means tags that occur in both the song and the profile.
    matched = song_tags & profile_tags
    # Union means every distinct tag in either collection, counted once.
    union = song_tags | profile_tags
    contributions = {}
    numerator = 0
    # Add each matching tag weight to the numerator and save its explanation.
    # Sorting here only makes the explanation repeatable.
    for tag in sorted(matched):
        # A missing dictionary entry uses the default weight of 1.
        weight = weights.get(tag, 1)
        contributions[tag] = weight
        numerator += weight
    denominator = 0
    # The denominator uses ALL union tags, not only matched preferences.
    # This is normalized weighted similarity rather than a raw weighted total.
    for tag in sorted(union):
        denominator += weights.get(tag, 1)
    # An empty union or all-zero union has no usable denominator.
    # Our explicit policy returns 0 instead of dividing by zero.
    if denominator == 0:
        score = 0.0
    else:
        score = numerator / denominator
    return score, contributions, denominator


def ranking_key(result):
    """Sort higher scores first and use ascending ID when scores tie."""
    # Python compares tuple keys from left to right.
    # Negative scores put larger original scores first in an ascending sort.
    # Only equal scores need the second key: ascending ID.
    return -result["score"], result["id"]


def rank_songs(songs, profile, weights, k=3):
    """Score every candidate, sort deterministically, and return at most k results."""
    require_limit(k)
    validate_weights(weights)
    # Build named records instead of making students remember tuple positions.
    scored = []
    for song in songs:
        tags = tags_for(song)
        # Unpack the three named results from the scoring function.
        score, contributions, denominator = weighted_similarity(tags, profile, weights)
        result = {
            "id": song["id"],
            "title": song.get("title", song["id"]),
            "score": score,
            "contributions": contributions,
            "union_weight": denominator,
        }
        scored.append(result)
    # First rank the entire eligible collection; never slice candidates first.
    ordered = sorted(scored, key=ranking_key)
    # A slice keeps at most k results. k=0 intentionally gives an empty list.
    return ordered[:k]


def main():
    """Compare ordinary and weighted shortlists after the same optional filter."""
    # Supplied interface wiring reuses argparse from Weeks 5 and 6.
    # This demo adds optional tag filtering and a maximum result count.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emphasis", choices=["calm", "piano"], default="calm")
    parser.add_argument("--tag", help="include only songs with this exact tag")
    parser.add_argument(
        "--limit", type=int, default=3, help="maximum results per list (default: 3)"
    )
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be zero or greater")
    # The profile is fixed while filters and weights change independently.
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
    # Keep the full ranking here so the display can report how many matches
    # were omitted and explain a tie that straddles the cutoff.
    baseline = rank_songs(candidates, profile, {}, len(candidates))
    show_results("Equal importance for each tag", baseline, args.limit)
    # Run the same candidates and profile again with one changed priority.
    weights = {args.emphasis: 4}
    weighted = rank_songs(candidates, profile, weights, len(candidates))
    show_results(
        f"Give {args.emphasis} extra importance (weight 4)", weighted, args.limit
    )
    # S02 and S05 share the same tags; ID settles their equal scores.
    # For --tag calm --limit 3, the tied pair straddles the cutoff.
    show_ties(weighted, args.limit)
    print("\nScore = matched tag weight / all distinct tag weight.")
    print("Other tags have weight 1; an empty or zero-weight union scores 0.")
    print(
        "These suggestions use fictional tags, not listening history or model training."
    )


if __name__ == "__main__":
    main()
