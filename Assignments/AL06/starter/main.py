"""Optional generic English-first scaffold for any one AL06 application."""

from scenario_data import SCENARIOS
from record_support import validate_node
from record_display import show_records, show_results

CHOICE = "fundraiser"  # Choose "fundraiser", "project", or "inventory".


# MONDAY — Decide what contributes, then follow the nested structure.

def recursive_total(node, included_status):
    """Return the selected entry amount or recursively combine a group's totals."""
    # Check this record with the supplied validate_node helper before selecting it.
    # If it is an entry, decide whether its status matches the supplied rule.
    # A qualifying entry contributes its amount; another valid entry contributes zero.
    # If it is a group, begin a fresh subtotal for this call.
    # Ask the same function about each child, passing the same required status.
    # Combine the returned numbers and return the completed group subtotal.
    # An empty group has nothing to add; leave the original records unchanged.
    raise NotImplementedError("Apply the entry rule and recursive aggregation.")


def iterative_total(node, included_status):
    """Total matching entries using an explicit stack without changing the source."""
    # Begin with the root as pending work and a running total.
    # While work remains, take one record from the end of the pending list.
    # Validate this record before applying the selection rule.
    # For an entry, add its amount only when its status meets the rule.
    # For a group, add its children as pending work; do not flatten in advance.
    # Return the selected total when all pending records have been processed.
    raise NotImplementedError("Apply the same rule using explicit pending work.")


def main():
    """Choose one context and present only the completed application stages."""
    scenario = SCENARIOS[CHOICE]
    # MONDAY: show_records can display the chosen data and its units.
    # Pass scenario["data"] and scenario["included_status"] to each completed function.
    # Pass the scenario and both numeric results to show_results.
    # Do not call unfinished functions just to produce a report.

    # EARLY TUESDAY: complete focused tests and brief normal README observations.
    # Check included/excluded entries at different depths and unchanged input.

    # Run your complete personal copy, commit/push, and submit before AL07 begins.
    print("AL06 starter — chosen application: " + scenario["title"])
    print("Begin with Monday's selected-entry rule and recursive function.")


if __name__ == "__main__":
    main()
