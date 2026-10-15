"""Supplied library records only; students implement their own lookup algorithms."""

BOOKS = [
    {"id": "B1", "title": "The Time Machine", "author": "H. G. Wells"},
    {"id": "B2", "title": "Frankenstein", "author": "Mary Shelley"},
    {"id": "B3", "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": "B4", "title": "The Secret Garden", "author": "Frances Hodgson Burnett"},
]


def validate_book_ids(records):
    """Reject unusable or duplicate book IDs before comparing lookup approaches."""
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each catalog record must be a dictionary.")
        book_id = record.get("id")
        if not isinstance(book_id, str) or not book_id.strip():
            raise ValueError("Each book needs a nonempty text ID.")
        if book_id in seen:
            raise ValueError("Duplicate book ID: " + book_id)
        seen.add(book_id)
