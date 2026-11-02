"""Optional English-first starter for stable sorting and a key-correct pipeline."""

from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets

# After preparing your local search_algorithms.py, add its search imports here.
# Copy your AL04 functions/imports, or use the instructor-released recovery module.


# TUESDAY - Stable ordering, with counts for one tiny example.

def insertion_sort(records, key):
    """Return a stable shallow ordered list, comparison/shift counts, and ID trace."""
    # Copy the outer list, sharing its record dictionaries. Start counts/trace.
    # Each position after the first introduces one item into the sorted prefix.
    # Save that item, then inspect earlier items from right to left.
    # Count each executed key comparison; shift only when the earlier key is larger.
    # Count right-shifts, not final placements. Stop shifting on equality.
    # Place the saved item in the gap. Record the entire ID order after insertion.
    # Return ordered list, comparisons, moves, and trace, even for empty input.
    raise NotImplementedError("Build the stable sorted prefix one item at a time.")


# THURSDAY - Compose existing interfaces; rebuild after the eligibility change.

def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists sharing eligible records."""
    # Use the supplied open/age filter on the authoritative source.
    # Use your insertion sort with days_key to build the display view.
    # Use sorted with id_key to build the separate binary-search view.
    # Return the three lists; do not copy records or edit their fields.
    raise NotImplementedError("Connect selection to two purposeful orderings.")


def main():
    """Present completed daily stages and explain the issued threshold change."""
    # TUESDAY: select open tickets aged at least 4 days; show stable age ordering.
    # Label the tiny ID trace and comparison/right-shift counts as teaching evidence.
    # Check your sort against sorted, including tied keys and unchanged source.

    # THURSDAY: build both views and use the local search_algorithms functions.
    # Find T403 and absent T499; resolve positions in the particular list searched.
    # Deliberately use the age display for ID binary search of T406; explain failure.
    # Rebuild from TICKETS at minimum_days=7, then 8, to show revised/empty results.
    # Keep app output readable; put short workload/copy/change notes in README.md.
    # Test and submit the complete personal week_04/AL05 folder independently.
    print("AL05 starter: begin with Tuesday's stable insertion sort.")


if __name__ == "__main__":
    main()
