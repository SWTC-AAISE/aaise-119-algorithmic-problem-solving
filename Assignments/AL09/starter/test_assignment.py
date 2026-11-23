"""Optional AL09 test scaffold: complete focused checks as each stage is taught."""

from copy import deepcopy
from math import isclose
from main import shared_count, jaccard, weighted_similarity, rank_resources, catalog_digest
from resource_data import RESOURCES, PROFILE, WEIGHTS, LIMITATION_ID
from resource_support import tags_for
from resource_display import same_recommendations

TEST_STAGE = 1  # Nov 23: 1; Nov 24: 2; Nov 30: 3 after adding those checks.


def test_small_comparison():
    """Completed example: predict overlap and union independently of the code."""
    left = ["queues", "collections"]
    right = ["queues", "stacks"]
    assert shared_count(left, right) == 1
    assert isclose(jaccard(left, right), 1 / 3)


def test_stage_1_boundaries():
    """Check repeated, missing, nonmatching and empty tags without changing inputs."""
    # Repeated copies of one tag count once; identical nonempty sets score 1.
    # No shared tags score 0; two empty collections also score 0 by our policy.
    # tags_for handles a resource with missing tags or tags=None as an empty set.
    # Use that supplied helper before comparing those cases with PROFILE.
    # Save independent copies of small inputs and check that neither changes.
    raise NotImplementedError("Add stage 1 boundary and preservation checks.")


def test_stage_2_rankings():
    """Check independent scores, the exact cutoff tie and changed preferences."""
    # Equal weights and k=2: expect LR013 then LR002.
    # Queue weight 4 and k=2: expect LR013 then LR003.
    # Independently check LR003: matched weight 4, union weight 6, score 4/6.
    # Check that its contributions identify queues with weight 4.
    # With k=3 and equal weights, LR002 precedes the tied LR003.
    # Reverse input order in a copy; the ranked results should stay the same.
    # Compare all-one weighted scores with independently expected Jaccard scores.
    raise NotImplementedError("Add stage 2 score, ranking and tie checks.")


def test_stage_2_boundaries():
    """Check limits, tag policies, zero weight and independent result records."""
    # k=0 and an empty catalog return []; a large k returns all available records.
    # Missing/None tags mean an empty set; repeated tags count once.
    # Empty or all-zero-weight unions score zero, without dividing by zero.
    # Preserve resources and nested tags, PROFILE and WEIGHTS using deepcopy.
    # Check required result fields and that changing a result does not edit input.
    # Supplied validation handles invalid weights/limits; do not build a framework.
    raise NotImplementedError("Add stage 2 boundary and preservation checks.")


def test_stage_3_controlled_changes():
    """Check separate missing-tag and title-only edits against independent expectations."""
    # Begin from independent deepcopy copies of RESOURCES for EACH experiment.
    # Remove tags only from LIMITATION_ID: expect equal-weight IDs LR002, LR003.
    # Check the original catalog remains unchanged and its original top two remain.
    # In a fresh copy, change only a title: the digest changes but recommendation
    # IDs, order and scores stay the same; same_recommendations compares those.
    # Reverse records and tag order in another copy: the digest stays the same.
    # The runner demonstrates these changes; add your own assertions here.
    raise NotImplementedError("Add stage 3 snapshot and recommendation checks.")


def main():
    """Run only the checks completed for the selected instructional stage."""
    if TEST_STAGE not in (1, 2, 3):
        raise ValueError("TEST_STAGE must be 1, 2, or 3")
    test_small_comparison()
    test_stage_1_boundaries()
    if TEST_STAGE >= 2:
        test_stage_2_rankings()
        test_stage_2_boundaries()
    if TEST_STAGE >= 3:
        test_stage_3_controlled_changes()
    print("Selected-stage checks passed; complete all three stages before submission.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    main()
