"""Supplied fictional folder records and small validation helpers for the demo."""

COURSE_FILES = {
    "type": "folder",
    "name": "Course Files",
    "items": [
        {"type": "file", "name": "notes.pdf", "size_mb": 4},
        {
            "type": "folder",
            "name": "Week 1",
            "items": [
                {"type": "file", "name": "slides.pdf", "size_mb": 6},
                {
                    "type": "folder",
                    "name": "Activities",
                    "items": [
                        {"type": "file", "name": "examples.zip", "size_mb": 10},
                    ],
                },
            ],
        },
    ],
}


def validate_item(item):
    """Reject malformed individual records; traversals check each visited item."""
    if not isinstance(item, dict) or not isinstance(item.get("name"), str):
        raise ValueError("Each item needs a name and a file/folder record.")
    if item.get("type") == "file":
        size = item.get("size_mb")
        if type(size) is not int or size < 0:
            raise ValueError("File sizes must be nonnegative whole MB; booleans are not sizes.")
    elif item.get("type") == "folder":
        if not isinstance(item.get("items"), list):
            raise ValueError("A folder needs a list of items, which may be empty.")
    else:
        raise ValueError("Item type must be file or folder.")
