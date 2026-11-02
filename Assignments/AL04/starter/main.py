"""Optional English-first starter for individual search contracts and correctness."""

from ticket_data import TICKETS
from search_support import id_key, category_key, matches, compare_values
from ticket_display import show_ticket, show_tickets, show_trace


# MONDAY - Separate the requested value from the traversal.

def linear_search(records, target, key=id_key):
    """Return the first matching position and visits, or None and visits."""
    # Begin an empty trace. Visit records in their existing order.
    # Select each record's value through key(record).
    # Remember its position and selected value before checking for a match.
    # Return the position and trace on a match; otherwise finish with None/trace.
    # Leave the records unchanged. An empty input has no visits.
    raise NotImplementedError("Implement the ordered scan.")


def binary_search(records, target, key=id_key):
    """Return any matching position and interval visits on a key-ordered input."""
    # The caller supplies a list ascending under the same key used here.
    # Begin with an empty trace and an inclusive interval covering the list.
    # While the interval contains candidates, select its integer midpoint.
    # Record low, high, middle, and the selected value before changing bounds.
    # Compare that value with target: match, lower, or higher.
    # Return on equality; otherwise discard the impossible side AND midpoint.
    # When no candidates remain, return None with the visits collected.
    # Do not sort or perform a sortedness scan inside this function.
    raise NotImplementedError("Implement interval narrowing.")


# TUESDAY CHECKPOINT - Verify the contract and preserve an independent submission.

def main():
    """Show completed searches with readable results and two small teaching traces."""
    # MONDAY: inspect TICKETS, then show found T403 and absent T499 using a scan.
    # Prepare an ID-ascending view outside binary_search; repeat those requests.
    # A result position belongs to the exact list searched; test `is None`.
    # Show one trace from each valid path with show_trace.
    # Deliberately search original unsorted data for T401; explain the miss.
    # Use category_key with a category-ordered view for repeated category account.
    # Accept any matching category record, not necessarily the same position.

    # TUESDAY: finish the boundary/duplicate/nonmutation tests and short README.
    # Run the final personal week_04/AL04 copy before submitting its repo URL.
    # Copy completed functions into AL05 later; preserve this submitted snapshot.
    print("AL04 starter: begin with Monday's linear search.")


if __name__ == "__main__":
    main()
