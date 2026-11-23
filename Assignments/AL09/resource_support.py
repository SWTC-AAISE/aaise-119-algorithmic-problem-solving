"""Supplied input checks and consistent snapshot serialization for AL09.

Snapshot contract: ID, title, URL, and unique sorted tags; records ordered by ID;
JSON keys ordered, compact separators, ASCII escapes, then UTF-8 bytes.
Source notes and other fields outside this contract are not fingerprinted.
"""

import json
from math import isfinite


def tags_for(resource):
    """Return distinct tags, treating missing or None tags as empty."""
    tags = resource.get("tags")
    if tags is None:
        return set()
    return set(tags)


def validate_weights(weights):
    """Require finite nonnegative numeric weights, excluding Boolean values."""
    for value in weights.values():
        if type(value) not in (int, float):
            raise ValueError("weights must be finite nonnegative numbers")
        if not isfinite(value) or value < 0:
            raise ValueError("weights must be finite nonnegative numbers")


def require_limit(k):
    """Require a nonnegative integer maximum result count."""
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative integer")


def resource_id_key(resource):
    """Return the ID used for consistent snapshot ordering."""
    return resource["id"]


def canonical_bytes(resources):
    """Serialize the declared fields consistently without changing the records."""
    normalized = []
    seen_ids = set()
    for resource in resources:
        resource_id = resource["id"]
        if resource_id in seen_ids:
            raise ValueError("duplicate resource IDs")
        seen_ids.add(resource_id)
        normalized.append({
            "id": resource_id,
            "title": resource["title"],
            "url": resource["url"],
            "tags": sorted(tags_for(resource)),
        })
    normalized.sort(key=resource_id_key)
    text = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return text.encode("utf-8")
