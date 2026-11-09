"""Find the total storage used by a folder, including all nested folders."""

from folder_data import COURSE_FILES, validate_item
from folder_display import show_folder
from console_style import print_color


def recursive_total(item):
    """Return a file's size or the combined size of everything in a folder."""
    validate_item(item)
    if item["type"] == "file":
        return item["size_mb"]

    total = 0
    for child in item["items"]:
        subtotal = recursive_total(child)
        total += subtotal
    return total


def iterative_total(item):
    """Return the same storage total using an explicit stack of pending items."""
    pending = [item]
    total = 0
    while pending:
        current = pending.pop()
        validate_item(current)
        if current["type"] == "file":
            total += current["size_mb"]
        else:
            for child in current["items"]:
                pending.append(child)
    return total


def main():
    """Show the folder contents and the two equivalent storage totals."""
    print_color(
        "\n===================================================================",
        "heading",
    )
    print_color("FOLDER STORAGE ANALYZER", "heading")
    print_color(
        "===================================================================\n",
        "heading",
    )
    print("How much space will Course Files need when we archive it?\n")
    show_folder(COURSE_FILES)

    total = recursive_total(COURSE_FILES)
    print_color(f"\nTotal storage: {total} MB", "success")
    checked_total = iterative_total(COURSE_FILES)
    print(f"Explicit-stack check: {checked_total} MB")
    print("\nEvery subfolder asks the same question: how much is inside me?")


if __name__ == "__main__":
    main()
