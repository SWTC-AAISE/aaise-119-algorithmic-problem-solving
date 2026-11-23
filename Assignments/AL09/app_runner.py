"""Supplied staged reports; students implement algorithms in main.py."""

from copy import deepcopy
from resource_data import RESOURCES, PROFILE, WEIGHTS, LIMIT, LIMITATION_ID
from resource_support import tags_for
from resource_display import show_baseline, show_ranking, show_change, same_recommendations, show_digest_pair
from console_style import print_color


def run(stage, shared_count, jaccard, rank_resources=None, catalog_digest=None):
    """Call completed student functions for the selected daily stage."""
    if stage not in (1, 2, 3):
        raise ValueError("STAGE must be 1, 2, or 3")
    print_color("FIND RESOURCES FOR A QUEUE AND STACK REVIEW", "heading")
    print("Profile: queues, stacks | Supplied catalog: eight Python references")
    print("Tags are teaching choices, not measured resource quality.")
    if stage == 1:
        rows = []
        for resource in RESOURCES:
            tags = tags_for(resource)
            rows.append({
                "id": resource["id"],
                "title": resource["title"],
                "count": shared_count(tags, PROFILE),
                "score": jaccard(tags, PROFILE),
                "matched": sorted(tags & PROFILE),
            })
        show_baseline(rows)
        print("\nTuesday adds ranked top-two results and weighted preferences.")
        return
    if rank_resources is None:
        raise ValueError("Pass your completed rank_resources function for stages 2 and 3")
    baseline = rank_resources(RESOURCES, PROFILE, {}, LIMIT)
    weighted = rank_resources(RESOURCES, PROFILE, WEIGHTS, LIMIT)
    show_ranking("Equal topic weights", baseline, len(RESOURCES), LIMIT)
    show_ranking("Give queues extra importance (weight 4)", weighted, len(RESOURCES), LIMIT)
    print("\nOrder: higher score first; equal scores use ascending ID.")
    print("LR002 and LR003 tie in the baseline; the ID rule settles the cutoff.")
    if stage == 2:
        print("Stage 3, Monday November 30, checks missing metadata and a title-only snapshot change.")
        return
    if catalog_digest is None:
        raise ValueError("Pass your completed catalog_digest function for stage 3")

    # STAGE 3 (Week 8 Monday): independent experimental copies, not persistent catalog edits.
    missing = deepcopy(RESOURCES)
    for resource in missing:
        if resource["id"] == LIMITATION_ID:
            resource["tags"] = []
    changed = rank_resources(missing, PROFILE, {}, LIMIT)
    show_ranking("After deque topic tags are missing", changed, len(missing), LIMIT)
    show_change("Recommendation IDs and scores", same_recommendations(baseline, changed))
    print("The reference itself did not change; its represented topics did.")

    renamed = deepcopy(RESOURCES)
    for resource in renamed:
        if resource["id"] == LIMITATION_ID:
            resource["title"] += " (display title edited)"
    renamed_ranking = rank_resources(renamed, PROFILE, {}, LIMIT)
    print_color("\nTitle-only edit, starting again from the original", "heading")
    show_change("Recommendation IDs and scores", same_recommendations(baseline, renamed_ranking))
    show_digest_pair(catalog_digest(RESOURCES), catalog_digest(renamed))
    print("\nThis checks selected metadata against our local reference.")
    print("It does not verify the web page contents, authenticity, or recommendation quality.")
