"""Presentation helpers only; students implement the AL03 ticket operations."""

from console_style import print_color


def display_tickets(title, records):
    """Show a readable ticket report without changing its supplied records."""
    print()
    print_color(title, "heading")
    if not records:
        print("No tickets to display.")
        return

    for record in records:
        print(f"{record['id']} - {record['title']}")
        print(
            f"  Category: {record['category']} | "
            f"Priority: {record['priority']} | Status: {record['status']}"
        )


def display_state(title, state):
    """Show live tickets, pending order, and the next reversible action."""
    records = []
    for ticket_id in state["registry"]:
        records.append(state["registry"][ticket_id])
    display_tickets(title, records)

    print_color("Waiting work (next first)", "heading")
    if not state["pending"]:
        print("No tickets waiting.")
    else:
        position = 1
        for ticket_id in state["pending"]:
            if ticket_id in state["registry"]:
                ticket = state["registry"][ticket_id]
                print(f"  {position}. {ticket_id} - {ticket['title']}")
            else:
                print_color(
                    f"  {position}. {ticket_id} - ticket no longer available",
                    "caution",
                )
            position += 1

    if state["undo"]:
        last_action = state["undo"][-1]
        ticket_id = last_action["ticket_id"]
        print(f"Undo available: return {ticket_id} to waiting work.")
    else:
        print("No processing action to undo.")
