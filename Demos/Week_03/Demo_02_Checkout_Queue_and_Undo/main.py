"""A FIFO request queue and a bounded LIFO checkout undo."""

from collections import deque

from console_style import print_color


def make_state():
    """Create separate inventory, waiting-request, and checkout-history containers."""
    inventory = {"E01": True, "E02": True}
    pending = deque()
    undo = []
    return {"inventory": inventory, "pending": pending, "undo": undo}


def enqueue(state, equipment_id):
    """Add one known equipment ID to the back of the waiting queue."""
    inventory = state["inventory"]
    pending = state["pending"]
    if equipment_id not in inventory:
        raise ValueError("unknown equipment ID")
    if equipment_id in pending:
        raise ValueError("duplicate pending request")
    pending.append(equipment_id)


def checkout_next(state):
    """Process the oldest request and save a successful checkout for undo."""
    inventory = state["inventory"]
    pending = state["pending"]
    undo = state["undo"]
    if not pending:
        return "queue empty"
    equipment_id = pending.popleft()
    previous_available = inventory[equipment_id]
    if not previous_available:
        return f"{equipment_id}: denied (unavailable); request consumed"
    inventory[equipment_id] = False
    change = {
        "equipment_id": equipment_id,
        "previous_available": previous_available,
    }
    undo.append(change)
    return f"{equipment_id}: checked out"


def undo_checkout(state):
    """Reverse the latest successful checkout and restore its waiting request."""
    inventory = state["inventory"]
    pending = state["pending"]
    undo = state["undo"]
    if not undo:
        return "nothing to undo"
    change = undo.pop()
    equipment_id = change["equipment_id"]
    previous_available = change["previous_available"]
    inventory[equipment_id] = previous_available
    # Restore the consumed request as well as inventory availability.
    if equipment_id not in pending:
        pending.appendleft(equipment_id)
    return f"{equipment_id}: checkout undone; request restored at front"


def display(state, action):
    """Show loan availability, waiting order, and the next reversible checkout."""
    inventory = state["inventory"]
    pending = state["pending"]
    undo = state["undo"]
    print_color(f"\n{action}", "heading")
    print("Equipment:")
    for equipment_id in inventory:
        if inventory[equipment_id]:
            print(f"  {equipment_id} - Ready to borrow")
        else:
            print(f"  {equipment_id} - On loan")
    print("Waiting requests (next first):")
    if not pending:
        print("  No requests waiting.")
    for equipment_id in pending:
        print(f"  {equipment_id}")
    if undo:
        latest_change = undo[-1]
        equipment_id = latest_change["equipment_id"]
        print(f"Next checkout that can be undone: {equipment_id}")
    else:
        print("No checkout available to undo.")


def main():
    """Process two loan requests, then reverse the most recent checkout."""
    print_color("EQUIPMENT CHECKOUT DESK", "heading")
    state = make_state()
    enqueue(state, "E01")
    enqueue(state, "E02")
    display(state, "Initial requests")
    display(state, checkout_next(state))
    display(state, checkout_next(state))
    display(state, undo_checkout(state))
    print("\nThe most recent checkout is undone first; FIFO request order is restored.")


if __name__ == "__main__":
    main()
