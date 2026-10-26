"""Documented companion to main.py; the service-update behavior is unchanged.

Thursday's lecture distinguishes a broken LIVE reference from a valid EARLIER
snapshot. Removing equipment does not automatically remove its pending request.
Likewise, creating a new list does not automatically copy the records inside it.
The comments connect repair ownership and copy choices to those two problems.
"""

from collections import deque
# deepcopy is guided library exposure, not an algorithm to reimplement. AL03's
# flat string-valued tickets need only individual record.copy() snapshots.
from copy import deepcopy

from console_style import print_color


def stale_ids(inventory, pending):
    """Return queued IDs missing from inventory, without changing either input.

    The rule is a relationship: every live waiting ID should have a live record.
    A deque of valid strings can still violate that application-level rule.
    """
    missing = []
    for equipment_id in pending:
        # Membership checks inventory keys, not record availability. This helper
        # repairs missing IDs only; it does not validate every possible state rule.
        if equipment_id not in inventory:
            missing.append(equipment_id)
    return missing


def repair_queue(inventory, pending):
    """Return (new repaired deque, missing IDs), leaving both inputs unchanged.

    Visit the original pending order and append only still-known IDs. Valid
    relative order is preserved without sorting, reversing, or consuming input.
    """
    removed = stale_ids(inventory, pending)
    repaired_queue = deque()
    for equipment_id in pending:
        if equipment_id in inventory:
            repaired_queue.append(equipment_id)
    # The caller receives two separate results. Returning a new deque does NOT
    # change the caller's pending variable or any state entry that holds it.
    return repaired_queue, removed


def display_queue(pending, heading):
    """Read and display waiting order with a clear empty-result message."""
    print(heading)
    if not pending:
        print("  No requests waiting.")
    # Iteration reads the queue; unlike popleft(), it does not consume requests.
    for equipment_id in pending:
        print(f"  {equipment_id}")


def display_availability(record, heading):
    """Translate one live or saved availability value into a readable loan status."""
    if record["available"]:
        status = "Ready to borrow"
    else:
        status = "On loan"
    print(f"  {heading}: {record['id']} - {status}")


def main():
    """Expose a stale request, show a repaired queue, and compare shared/copied records."""
    print_color("EQUIPMENT SERVICE UPDATE", "heading")
    # This demo uses full record dictionaries again. Tuesday simplified inventory
    # values to Booleans; the ID-to-record relationship is explicit here.
    inventory = {"E01": {"id": "E01", "available": True},
                 "E02": {"id": "E02", "available": True}}
    pending = deque(["E01", "E02"])
    display_queue(pending, "Waiting requests before the service update:")
    # Break the rule deliberately: only the dictionary changes. The separate
    # queue still contains E02, even though its equipment record is now gone.
    del inventory["E02"]
    print_color("\nE02 has been removed from inventory.", "caution")
    missing_ids = stale_ids(inventory, pending)
    for equipment_id in missing_ids:
        print(f"  Request needs attention: {equipment_id} is no longer in inventory.")
    # Unpack the two returned results into their own named variables.
    repaired, removed = repair_queue(inventory, pending)
    for equipment_id in removed:
        print(f"  Closed request for removed equipment: {equipment_id}")
    display_queue(repaired, "Waiting requests after repair:")
    # IMPORTANT: this demo displays the NEW queue; pending itself is unchanged.
    # In AL03, the owning application must install the returned queue:
    # state["pending"] = repaired
    # That owner step is taught in the lecture, not executed by this standalone
    # demo. An older alias would still point to the original deque afterward.

    # A new outer list still holds references to the original dictionaries.
    # At this point inventory contains only E01, so aliases[0] is that same record.
    aliases = []
    for equipment_id in inventory:
        aliases.append(inventory[equipment_id])
    # Copy the list AND its contained records for this ordinary data example.
    # Taking the snapshot BEFORE the checkout preserves the earlier ready value.
    snapshot = deepcopy(aliases)
    inventory["E01"]["available"] = False
    print_color("\nE01 has now been checked out.", "heading")
    # Current and alias views both reach the changed record: both say On loan.
    display_availability(inventory["E01"], "Current inventory")
    display_availability(aliases[0], "New list, same record")
    # The snapshot's separate record still says Ready to borrow. That difference
    # is intentional historical information, not a missing live-queue reference.
    display_availability(snapshot[0], "Independent saved snapshot")
    print("  The saved snapshot is independent, not read-only.")
    # Independence does not prohibit editing the snapshot itself. Its edits do
    # not need to change current inventory. Regression checks stay in test_demo.py.


if __name__ == "__main__":
    main()
