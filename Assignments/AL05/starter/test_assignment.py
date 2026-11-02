"""Unfinished prompts for sort stability, pipeline contracts, and rule revision."""

from copy import deepcopy
from main import insertion_sort, build_views
from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets


def assignment_checks():
    """Check expected orders, stable ties, shared records, and rebuilt query views."""
    # TUESDAY: test empty/singleton, ordered/reverse/shuffled inputs, and stable ties.
    # Compare output with sorted under the same key; source order/fields stay intact.
    # Check new outer list and shared record identities, using `is` where useful.
    # Check the small fixture's expected counts and ID trace, not timing.
    # THURSDAY: check exact selected/display/search IDs at thresholds 4, 7, and 8.
    # Include boundary ages and completed-ticket exclusion; rebuild from TICKETS.
    # Import your local searches when ready: test found/missing and view positions.
    # Mark wrong-view T406 as deliberate invalid use, separate from valid contracts.
    # Use a separate fixture copy if testing a field edit; do not alter shared seed.
    raise NotImplementedError("Replace these prompts with your completed assertions.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL05 checks passed.")
