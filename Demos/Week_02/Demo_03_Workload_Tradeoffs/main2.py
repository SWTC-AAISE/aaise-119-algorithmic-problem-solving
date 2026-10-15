"""Compact index equivalents for the qualitative workload demonstration."""

import main as explicit

"""
AI Explanation Prompt - Dictionary/list comprehensions and dict.get()
Compare indexed with main.py's loops. Explain index construction, missing IDs,
and query order. Why does the build remain O(n), while one existing-index
lookup is average-case O(1)? Do not benchmark or claim a universal winner.
"""


def indexed(records, queries):
    """Return equivalent ordered answers from a newly built ID index."""
    index = {record["id"]: record for record in records}
    return [index.get(query) for query in queries]


def make_records(size):
    """Create the same small unique-ID fixture with a comprehension."""
    return [{"id": value} for value in range(size)]


def main():
    """Reuse the recognition display with compact equivalents."""
    explicit.run_demo(index_function=indexed, record_builder=make_records)


if __name__ == "__main__":
    main()
