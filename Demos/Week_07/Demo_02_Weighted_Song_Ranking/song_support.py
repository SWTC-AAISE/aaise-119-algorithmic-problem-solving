"""Supplied data and input checks; the lesson focuses on filtering and ranking."""

from math import isfinite


def tags_for(song):
    """Treat missing or None tags as an empty set for this demonstration."""
    tags = song.get("tags")
    if tags is None:
        return set()
    return set(tags)


def validate_weights(weights):
    """Reject nonnumeric, infinite, negative, or Boolean tag weights."""
    for value in weights.values():
        if type(value) not in (int, float):
            raise ValueError("weights must be finite nonnegative numbers")
        if not isfinite(value) or value < 0:
            raise ValueError("weights must be finite nonnegative numbers")


def require_limit(k):
    """Require a nonnegative integer result limit, including an intentional zero."""
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative integer")
