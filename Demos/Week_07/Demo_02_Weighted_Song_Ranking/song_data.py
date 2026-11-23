"""Small fictional song catalog, including a deliberate nonzero-score tie."""

# S05 deliberately precedes S02: input order must not decide their tied ranks.
SONGS = [
    {"id": "S01", "title": "Quiet Keys", "tags": ["calm", "piano"]},
    {"id": "S05", "title": "Gentle Guitar", "tags": ["calm", "acoustic"]},
    {"id": "S02", "title": "Soft Strings", "tags": ["calm", "acoustic"]},
    {"id": "S03", "title": "Piano Focus", "tags": ["piano"]},
    {"id": "S04", "title": "Unknown Track", "tags": []},
    {"id": "S06", "title": "Evening Keys", "tags": ["calm", "piano", "jazz"]},
]
