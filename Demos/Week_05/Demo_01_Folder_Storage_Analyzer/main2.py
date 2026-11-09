"""Documented equivalent of main.py: the same folder data, results, and algorithms.

Read main.py first to see the small algorithm. Use this companion when you want
the call/return reasoning and the connection to a familiar list stack explained.
"""

from folder_data import COURSE_FILES, validate_item
from folder_display import show_folder
from console_style import print_color


def recursive_total(item):
    """Return a file's size or the combined size of everything in a folder."""
    # The supplied helper checks this one record; it does not total its contents.
    validate_item(item)
    # BASE CASE: a file already tells us its size, so no smaller call is needed.
    if item["type"] == "file":
        return item["size_mb"]

    # RECURSIVE CASE: every item inside the folder follows this same rule.
    # Each function call owns a separate local total; the calls do not share it.
    total = 0
    for child in item["items"]:
        # Pause THIS call while the child is handled; its returned value is a number.
        # A folder child can ask about its own children before returning its subtotal.
        subtotal = recursive_total(child)
        total += subtotal
    # An empty folder also works: zero loop iterations leave total at zero.
    # Return to the caller that was waiting for this folder's answer.
    return total


def iterative_total(item):
    """Return the same storage total using an explicit stack of pending items."""
    # Store unfinished work in a familiar list instead of recursive function calls.
    pending = [item]
    total = 0
    while pending:
        # pop() takes the last item: the LIFO behavior reviewed in Week 3.
        current = pending.pop()
        validate_item(current)
        if current["type"] == "file":
            total += current["size_mb"]
        else:
            # Add each child for later handling; do not pre-flatten the data.
            # The last child added is processed first. Addition gives the same total
            # even though this visiting order differs from the recursive version.
            for child in current["items"]:
                pending.append(child)
    return total


def main():
    """Show the folder contents and the two equivalent storage totals."""
    # Establish why someone needs this answer before opening the algorithm functions.
    # Supplied records stand in for files, so no filesystem API is needed.
    print_color("FOLDER STORAGE ANALYZER", "heading")
    print("How much space will Course Files need when we archive it?\n")
    show_folder(COURSE_FILES)

    # The same function handles a file, a folder, or another nesting level.
    total = recursive_total(COURSE_FILES)
    print_color(f"\nTotal storage: {total} MB", "success")
    # Pass the same source to the alternative; neither algorithm changes it.
    checked_total = iterative_total(COURSE_FILES)
    print(f"Explicit-stack check: {checked_total} MB")
    print("\nEvery subfolder asks the same question: how much is inside me?")


if __name__ == "__main__":
    main()
