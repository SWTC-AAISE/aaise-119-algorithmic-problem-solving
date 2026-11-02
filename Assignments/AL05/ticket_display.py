"""Reusable presentation only; no search, filtering, or sorting algorithms."""

from console_style import print_color


def show_ticket(record):
    """Show a ticket's useful details or a clear missing-result message."""
    if record is None:
        print_color("  No matching ticket found.", "caution")
        return
    print(f"  {record['id']} - {record['title']}")
    print(f"    Category: {record['category']} | Days open: {record['days_open']}")
    print(f"    Priority: {record['priority']} | Status: {record['status']}")


def show_tickets(title, records):
    """Present an ordered ticket selection without changing it."""
    print_color("\n" + title, "heading")
    if not records:
        print("  No tickets in this selection.")
    for record in records:
        show_ticket(record)


def show_trace(title, trace):
    """Label the small search trace as an instructional view, not the main report."""
    print_color("\nTeaching view: " + title, "heading")
    if not trace:
        print("  No records visited.")
    for step in trace:
        if len(step) == 2:
            print(f"  Position {step[0]}: checked {step[1]}")
        else:
            print(f"  Bounds {step[0]} to {step[1]}; midpoint {step[2]}: checked {step[3]}")
