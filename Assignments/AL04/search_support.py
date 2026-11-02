"""Supplied selectors and comparison rules; students implement the traversals."""


def id_key(record):
    """Select the unique ticket ID."""
    return record["id"]


def category_key(record):
    """Select the category, which can repeat across tickets."""
    return record["category"]


def days_key(record):
    """Select the number of days open for display ordering."""
    return record["days_open"]


def matches(value, target):
    """Decide whether a selected value equals the requested value."""
    return value == target


def compare_values(value, target):
    """Return -1, 0, or 1 for smaller, equal, or larger comparable values."""
    if matches(value, target):
        return 0
    if value < target:
        return -1
    return 1
