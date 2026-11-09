"""Unfinished generic test prompts for whichever AL06 application you choose."""

from copy import deepcopy
from main import CHOICE, recursive_total, iterative_total
from scenario_data import SCENARIOS, make_entry, make_group


def assignment_checks():
    """Check selected totals, boundary/nested cases, invalid data, and preservation."""
    scenario = SCENARIOS[CHOICE]
    # MONDAY: use the chosen app's independently expected total from the assignment.
    # Check each algorithm against that number, not only against the other algorithm.
    # Use make_entry/make_group to build small fixtures for your chosen statuses.

    # TUESDAY: check an included entry, excluded entry, zero, empty/flat groups,
    # mixed nesting, and an additional containing group.
    # Include equal amounts with different statuses, plus a group with no matches.
    # Preserve a deepcopy of the original; compare after both traversals.
    # Check ValueError for malformed data, even when its status would exclude it.
    # Keep assertions here rather than inside normal application output.
    raise NotImplementedError("Replace these prompts with your focused assertions.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run tests without -O so assertions remain enabled.")
    assignment_checks()
    print("AL06 checks passed.")
