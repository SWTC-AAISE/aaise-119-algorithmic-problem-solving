"""Four supplied code patterns for recognition, not performance measurement."""


def first_id(records):
    """Return the first ID, or None for an empty list."""
    if not records:
        return None
    return records[0]["id"]


def all_ids(records):
    """Collect each catalog ID once in input order."""
    identifiers = []
    for record in records:
        identifiers.append(record["id"])
    return identifiers


def ordered_pairs(records):
    """Create every ordered pair of IDs, including self-pairs."""
    pairs = []
    for first in records:
        for second in records:
            pairs.append((first["id"], second["id"]))
    return pairs


def halving_sizes(size):
    """Illustrate repeated halving of a nonnegative whole-number size."""
    if type(size) is not int or size < 0:
        raise ValueError("Use a nonnegative whole-number size.")
    sizes = []
    while size > 1:
        sizes.append(size)
        size = (size + 1) // 2
    if size == 1:
        sizes.append(size)
    return sizes
