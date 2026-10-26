"""Optional unfinished test scaffold; students choose expected ticket behavior."""

from collections import deque

from main import (
    build_registry,
    scan_lookup,
    indexed_lookup,
    update_priority,
    filter_by_category,
    enqueue_ticket,
    process_next,
    undo_process,
    repair_queue,
    cancel_ticket,
)
from ticket_data import TICKETS, SUPPORTED_CATEGORIES


def assignment_checks():
    """Check the implemented daily contracts against independent expectations."""
    # MONDAY - Start with fresh records for each independent example.
    # Predict found, missing, and empty-input results before calling the functions.
    # Check duplicate-ID rejection without changing the supplied TICKETS.
    # Check that priority edits affect only the intended live record.
    # Check supported-category membership, matching records, and empty selections.
    # Edit a copied selection and check that live/supplied records stay unchanged.
    # Example assertion syntax only: assert 2 + 2 == 4

    # TUESDAY - Begin after Tuesday's instruction.
    # Build fresh state with an empty pending deque and undo list.
    # Check acceptance of open tickets and rejection of unknown/completed/queued IDs.
    # For rejected actions, compare registry, pending, and history before/after.
    # Process two IDs and predict which one a single undo restores first.
    # Check successive undo, empty queue/history, and preserved priority edits.
    # Save before-state values independently; an alias changes with live state.

    # THURSDAY - Begin after Thursday's instruction.
    # Check cancellation of open tickets both pending and not pending.
    # Check missing/completed cancellation leaves every state component unchanged.
    # Repair mixed, empty, all-valid, and all-missing queues; check retained order.
    # Check the original queue is unchanged and the returned queue is installed.
    # Save a copied selection, then update/cancel live tickets and check old values.
    # Rerun the earlier checks after adding these operations.

    # Add actual assertions for each stage as you complete it.
    # Remove this exception only after adding real executable checks.
    raise NotImplementedError("Add focused checks before reporting success.")


def main():
    """Reject unfinished or disabled tests before reporting success."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
