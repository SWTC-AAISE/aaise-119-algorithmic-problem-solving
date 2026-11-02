"""Instructor-controlled AL05 recovery; release only after the AL04 checkpoint decision.

Supplied search code is not the student's assessed AL04 implementation. Copy
this module beside AL05 main.py only when released; do not import across folders.
"""

from search_support import id_key, matches, compare_values


def linear_search(records, target, key=id_key):
    """Return a first matching view position and trace, or None and the visit trace."""
    trace = []
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace


def binary_search(records, target, key=id_key):
    """Return any match and trace, assuming ascending order under the selected key."""
    low = 0
    high = len(records) - 1
    trace = []
    while low <= high:
        middle = (low + high) // 2
        value = key(records[middle])
        trace.append((low, high, middle, value))
        comparison = compare_values(value, target)
        if comparison == 0:
            return middle, trace
        if comparison < 0:
            low = middle + 1
        else:
            high = middle - 1
    return None, trace
