"""Supplied eligibility only; students implement stable sorting and composition."""


def select_open_tickets(records, minimum_days=4):
    """Return a new list sharing open records at or above the inclusive age limit."""
    selected = []
    for record in records:
        if record["status"] == "open" and record["days_open"] >= minimum_days:
            selected.append(record)
    return selected
