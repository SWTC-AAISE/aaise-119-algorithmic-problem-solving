"""Supplied missing-tag policy, separate from similarity calculations."""


def tags_for(song):
    """Return distinct tags, treating missing or None tags as empty."""
    tags = song.get("tags")
    if tags is None:
        return set()
    return set(tags)
