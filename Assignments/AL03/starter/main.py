"""Optional English-first starter; develop one ticket application across three days."""

from collections import deque  # Used beginning Tuesday.

from ticket_data import TICKETS, SUPPORTED_CATEGORIES
from ticket_display import display_tickets, display_state


# ======================================================================
# MONDAY - Find, update, and select
# Begin after Monday's instruction. Work in this same file all week.
# ======================================================================

def build_registry(records):
    """Return independent ticket records indexed by unique ID."""
    # Begin with an empty dictionary and visit each supplied record.
    # If its ID is already present, raise ValueError rather than overwrite it.
    # Otherwise, store a flat copy of the record under that ID.
    # Return the dictionary; leave the supplied records unchanged.
    raise NotImplementedError("Build the independent ticket registry.")


def scan_lookup(records, ticket_id):
    """Return the first matching ticket, or None when absent."""
    # Visit the records in order, comparing each ID with the requested ID.
    # Return the first match; return None if no record matches.
    raise NotImplementedError("Find a ticket using a list scan.")


def indexed_lookup(registry, ticket_id):
    """Return the matching live ticket, or None when absent."""
    # Check whether the requested ID is a key in the existing registry.
    # Return its record when present, or None when missing. Do not rebuild it.
    raise NotImplementedError("Find a ticket using its registry key.")


def update_priority(registry, ticket_id, priority):
    """Update one existing ticket's priority and report whether it was found."""
    # First check whether the ticket exists; if missing, return False unchanged.
    # Change only its priority field, then return True.
    raise NotImplementedError("Update the requested ticket's priority.")


def filter_by_category(registry, category):
    """Return independent copies of tickets matching the selected category."""
    # Start an empty result list and visit the live records in registry order.
    # For each matching category, append a flat record copy, not the live record.
    # Return the list; no matches means an empty list.
    raise NotImplementedError("Select copied tickets by category.")


# ======================================================================
# TUESDAY - Process in order and undo one action
# Wait until Tuesday's instruction before beginning this stage.
# ======================================================================

def enqueue_ticket(state, ticket_id):
    """Queue a known open ticket once, returning whether it was accepted."""
    # Check that the ID exists, its ticket is open, and it is not already waiting.
    # If any check fails, return False without changing any part of state.
    # Otherwise, add the ID at the back of pending and return True.
    raise NotImplementedError("Add an eligible ticket to waiting work.")


def process_next(state):
    """Complete the oldest waiting ticket and remember its previous status."""
    # If pending is empty, return None without changing state.
    # Take the oldest ID from the front of pending and find its live ticket.
    # Append a history record with named ticket_id and previous_status fields.
    # Mark the ticket completed and return its ID.
    raise NotImplementedError("Process the oldest pending request.")


def undo_process(state):
    """Restore the latest processed ticket and return it to the queue front."""
    # If history is empty, return None without changing state.
    # Remove the newest history record and use its named fields to find the ticket.
    # Restore only its prior status; keep unrelated priority changes.
    # Return the ID to the front of pending, then return that ID to the caller.
    raise NotImplementedError("Undo the latest successful processing action.")


# ======================================================================
# THURSDAY - Cancel consistently and preserve snapshots
# Wait until Thursday's instruction before beginning this stage.
# ======================================================================

def repair_queue(registry, pending):
    """Return a new queue of known IDs and a list of removed missing IDs."""
    # Prepare a new empty deque and a list for removed IDs.
    # Visit pending in order: keep known IDs in the new queue, collect missing IDs.
    # Return both collections without changing registry or the original pending.
    # The owning application must install the returned queue into its state.
    raise NotImplementedError("Repair missing-ticket references without reordering.")


def cancel_ticket(state, ticket_id):
    """Remove an open ticket and any waiting request, leaving history unchanged."""
    # Check existence and open status before making any changes.
    # Return False unchanged for a missing or completed ticket.
    # Remove the eligible ticket from the registry and remove its pending reference.
    # You may reuse repair_queue, installing its returned queue into state.
    # Leave other requests in order and history unchanged; return True.
    raise NotImplementedError("Cancel an open ticket consistently.")


def main():
    """Show only the daily stages whose operations you have completed."""
    # MONDAY: build a fresh registry from TICKETS.
    # Compare scan/index answers before edits; display a found or missing result.
    # Update one priority. Check a category using SUPPORTED_CATEGORIES membership.
    # Select copied category records and show them using display_tickets.
    # Keep a selection to revisit later; do not call unfinished later-day functions.

    # TUESDAY: add a state dictionary with registry, pending deque, and undo list.
    # Queue two open IDs; process both in arrival order; undo the last processing.
    # Use display_state to make waiting work and restoration clear.
    # Reject unknown, completed, and duplicate pending requests without changes.

    # THURSDAY: use a separate stale-queue example and install its repaired queue.
    # Demonstrate open-ticket cancellation and unchanged state for rejected actions.
    # Compare an earlier saved selection with the registry after update/cancellation.
    # Run all tests, add brief personal README notes, and commit progress.
    # Each partner tests a full personal copy and submits their own repository URL.

    # Replace this message as your Monday baseline becomes ready.
    print("AL03 starter: begin with the Monday section.")


if __name__ == "__main__":
    main()
