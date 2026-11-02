"""Unfinished test prompts; replace the final stop with your own focused checks."""

from copy import deepcopy
from main import linear_search, binary_search
from ticket_data import TICKETS
from search_support import id_key, category_key


def assignment_checks():
    """Check independent expected answers, boundaries, traces, and input preservation."""
    # MONDAY: use a separate fixture copy and an independently expected found ID.
    # Check missing, empty, singleton, first/last ID, and valid position zero.
    # Prepare ID order for binary tests. Check absent below/between/above IDs.
    # Check trace contents include the matching visit and actual input values.
    # TUESDAY: use category order and accept any matching duplicate category.
    # Check unchanged input order/fields, including after unsuccessful searches.
    # Separately demonstrate T401's deliberate invalid-order miss on TICKETS.
    # Agreement between two implementations alone is not an independent oracle.
    raise NotImplementedError("Replace these prompts with your completed assertions.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL04 checks passed.")
