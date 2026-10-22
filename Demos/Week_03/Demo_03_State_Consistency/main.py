"""Expose stale references and distinguish shallow aliases from snapshots."""

from collections import deque
from copy import deepcopy

from console_style import print_color


def stale_ids(inventory, pending):
    """Find waiting requests whose equipment no longer exists in inventory."""
    missing = []
    for equipment_id in pending:
        if equipment_id not in inventory:
            missing.append(equipment_id)
    return missing


def repair_queue(inventory, pending):
    """Build a repaired queue without changing the caller's original queue."""
    removed = stale_ids(inventory, pending)
    repaired_queue = deque()
    for equipment_id in pending:
        if equipment_id in inventory:
            repaired_queue.append(equipment_id)
    return repaired_queue, removed


def display_queue(pending, heading):
    """List requests in waiting order without exposing container notation."""
    print(heading)
    if not pending:
        print("  No requests waiting.")
    for equipment_id in pending:
        print(f"  {equipment_id}")


def display_availability(record, heading):
    """Label a live or saved equipment record with its readable loan status."""
    if record["available"]:
        status = "Ready to borrow"
    else:
        status = "On loan"
    print(f"  {heading}: {record['id']} - {status}")


def main():
    """Repair a removed-equipment request and compare live records with a snapshot."""
    print_color("EQUIPMENT SERVICE UPDATE", "heading")
    inventory = {"E01": {"id": "E01", "available": True},
                 "E02": {"id": "E02", "available": True}}
    pending = deque(["E01", "E02"])
    display_queue(pending, "Waiting requests before the service update:")
    del inventory["E02"]
    print_color("\nE02 has been removed from inventory.", "caution")
    missing_ids = stale_ids(inventory, pending)
    for equipment_id in missing_ids:
        print(f"  Request needs attention: {equipment_id} is no longer in inventory.")
    repaired, removed = repair_queue(inventory, pending)
    for equipment_id in removed:
        print(f"  Closed request for removed equipment: {equipment_id}")
    display_queue(repaired, "Waiting requests after repair:")

    # A new outer list still refers to the original record dictionaries.
    aliases = []
    for equipment_id in inventory:
        aliases.append(inventory[equipment_id])
    # deepcopy also copies the records, preserving their values for comparison.
    snapshot = deepcopy(aliases)
    inventory["E01"]["available"] = False
    print_color("\nE01 has now been checked out.", "heading")
    display_availability(inventory["E01"], "Current inventory")
    display_availability(aliases[0], "New list, same record")
    display_availability(snapshot[0], "Independent saved snapshot")
    print("  The saved snapshot is independent, not read-only.")


if __name__ == "__main__":
    main()
