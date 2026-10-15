"""Compact first-match search beside the explicit recognition example."""

import main as explicit

"""
AI Explanation Prompt - Generator expression and next()
Explain how find_record searches lazily, stops at the first match, and returns
None when absent. Compare it with main.py's loop and return. Does it build a
list of all matches? Do not rewrite, optimize, or benchmark the code.
"""


def find_record(records, target):
    """Return the same first match using a generator and a None default."""
    return next((record for record in records if record["id"] == target), None)


"""
AI Explanation Prompt - List comprehension
Compare make_records with the explicit loop in main.py. Explain the list and
dictionary produced for each value. Do not claim compact syntax changes Big-O.
"""


def make_records(size):
    """Build the same small unique-ID fixture compactly."""
    return [{"id": value} for value in range(size)]


def main():
    """Reuse the same recognition examples with compact equivalents."""
    explicit.run_demo(finder=find_record, record_builder=make_records)


if __name__ == "__main__":
    main()
