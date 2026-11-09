"""Supplied presentation helper; the storage algorithms remain in main.py."""

from folder_data import validate_item


def show_folder(item):
    """Display named files and folders in input order with readable indentation."""
    pending = [(item, 0)]
    while pending:
        current, depth = pending.pop()
        validate_item(current)
        indent = "  " * depth
        if current["type"] == "file":
            print(f"{indent}- {current['name']} ({current['size_mb']} MB)")
        else:
            print(f"{indent}{current['name']}/")
            for child in reversed(current["items"]):
                pending.append((child, depth + 1))
