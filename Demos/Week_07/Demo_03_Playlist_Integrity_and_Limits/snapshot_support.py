"""Supplied serialization contract for consistent local metadata comparisons.

Canonical means a consistent representation under our chosen rules:
include ID, title, and unique sorted tags; sort records by ID; sort JSON keys;
omit extra spacing; use ASCII escapes for JSON text and encode as UTF-8 bytes.
Record order and tag order do not change the snapshot. Titles do.

AI explanation prompt: Explain json.dumps(), encode("utf-8"), and bytes in this
helper. Why can different text formatting change a digest of the same records?
"""

import json


def tags_for(song):
    """Return distinct tags, treating missing or None tags as empty."""
    tags = song.get("tags")
    if tags is None:
        return set()
    return set(tags)


def song_id_key(song):
    """Return the stable record ID used for canonical ordering."""
    return song["id"]


def canonical_bytes(playlist):
    """Serialize the declared fields into reproducible bytes without editing input."""
    seen_ids = set()
    normalized = []
    for song in playlist:
        song_id = song["id"]
        if song_id in seen_ids:
            raise ValueError("duplicate song IDs")
        seen_ids.add(song_id)
        normalized.append({
            "id": song_id,
            "title": song["title"],
            "tags": sorted(tags_for(song)),
        })
    normalized.sort(key=song_id_key)
    text = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    encoded = text.encode("utf-8")
    return encoded
