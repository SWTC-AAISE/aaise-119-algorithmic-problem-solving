"""Documented companion to main.py; the checkout behavior is unchanged.

Tuesday's lecture separates three responsibilities: current availability,
FIFO waiting work, and LIFO successful history. The comments follow the same
before/process/process/undo sequence as the lecture's four-row state table.
This is undo for one action type, not a general undo/redo system.
"""

# deque (pronounced "deck") provides operations at both ends. The operations
# we CHOOSE establish FIFO behavior; the container alone does not enforce it.
from collections import deque

from console_style import print_color


def make_state():
    """Create fresh inventory, pending requests, and successful checkout history.

    Inventory values here are availability Booleans, a simplification from
    Monday's full records. AL03 keeps full tickets with status fields instead.
    Pending holds IDs; undo holds named-field change records, not pending work.
    """
    inventory = {"E01": True, "E02": True}
    pending = deque()
    undo = []
    return {"inventory": inventory, "pending": pending, "undo": undo}


def enqueue(state, equipment_id):
    """Append a known ID once, raising ValueError for unknown or duplicate requests.

    This demo permits a known unavailable item to be queued; checkout handles
    that denial. AL03 instead rejects completed tickets before enqueueing.
    """
    # These local names refer to the SAME containers held in state. They do
    # not copy them, so appending to pending changes state['pending'] too.
    inventory = state["inventory"]
    pending = state["pending"]
    if equipment_id not in inventory:
        raise ValueError("unknown equipment ID")
    if equipment_id in pending:
        raise ValueError("duplicate pending request")
    # append() puts a request at the back, behind already waiting requests.
    # Checking for duplicates may scan pending; a constant-time endpoint append
    # does not make this entire function constant-time.
    pending.append(equipment_id)


def checkout_next(state):
    """Process the oldest request and remember only a successful checkout.

    Returns:
        A message describing an empty queue, a denied request, or a checkout.
        Denial consumes the waiting request but does not create undo history.
    """
    inventory = state["inventory"]
    pending = state["pending"]
    undo = state["undo"]
    # An empty deque has no front item: stop without changing any state.
    if not pending:
        return "queue empty"
    # Pair back insertion with front removal: the oldest request leaves first.
    equipment_id = pending.popleft()
    # Save the OLD value before mutation. Saving False after a successful
    # checkout would not tell undo how to restore the earlier ready state.
    previous_available = inventory[equipment_id]
    if not previous_available:
        # The queue has already lost this request. Inventory stays unavailable,
        # and this unsuccessful checkout must not enter successful history.
        return f"{equipment_id}: denied (unavailable); request consumed"
    inventory[equipment_id] = False
    # Named fields make the reversible change readable without tuple positions.
    # Remember only what this action needs, not an entire unrelated record edit.
    change = {
        "equipment_id": equipment_id,
        "previous_available": previous_available,
    }
    # Appending makes this the newest successful action, at the list's end.
    undo.append(change)
    return f"{equipment_id}: checked out"


def undo_checkout(state):
    """Reverse the latest successful checkout and restore its waiting request.

    Restoration coordinates inventory, the queue, and history. Restoring only
    availability would lose the request that checkout previously consumed.
    """
    inventory = state["inventory"]
    pending = state["pending"]
    undo = state["undo"]
    if not undo:
        return "nothing to undo"
    # pop() removes AND returns the last item: LIFO successful-action history.
    change = undo.pop()
    equipment_id = change["equipment_id"]
    previous_available = change["previous_available"]
    inventory[equipment_id] = previous_available
    # Return the consumed request to the FRONT, not behind newer waiting work.
    # The membership guard avoids adding a second copy if the ID is already there.
    if equipment_id not in pending:
        pending.appendleft(equipment_id)
    return f"{equipment_id}: checkout undone; request restored at front"


def display(state, action):
    """Show current availability, waiting order, and the next reversible checkout.

    This function reads state without processing requests or changing history.
    Meaningful labels, rather than raw containers, make the desk usable.
    """
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
        # [-1] READS the last history item; unlike pop(), it does not remove it.
        latest_change = undo[-1]
        equipment_id = latest_change["equipment_id"]
        print(f"Next checkout that can be undone: {equipment_id}")
    else:
        print("No checkout available to undo.")


def main():
    """Run the lecture's initial/process/process/undo example without extra tracing."""
    print_color("EQUIPMENT CHECKOUT DESK", "heading")
    state = make_state()
    enqueue(state, "E01")
    enqueue(state, "E02")
    # Initial row: both ready; waiting E01, E02; successful history empty.
    display(state, "Initial requests")
    # Python evaluates the inner call first: change state, receive its message,
    # then display that message alongside the resulting state.
    # Process E01: E01 on loan; waiting E02; successful history contains E01.
    display(state, checkout_next(state))
    # Process E02: both on loan; no waiting work; history contains E01 then E02.
    display(state, checkout_next(state))
    # Undo once: E02 ready and waiting first; E01 remains on loan/in history.
    display(state, undo_checkout(state))
    print("\nThe most recent checkout is undone first; FIFO request order is restored.")
    # Empty/unknown/duplicate/denied cases are checked separately in test_demo.py.
    # No assertions, extra trace output, or general undo machinery are added here.


if __name__ == "__main__":
    main()
