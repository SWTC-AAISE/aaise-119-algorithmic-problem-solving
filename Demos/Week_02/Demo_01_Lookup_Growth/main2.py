"""Compact equivalents of Monday's loops; the experiment stays the same."""

import main as explicit


"""
AI Explanation Prompt - List comprehension
Explain how make_records builds a list of dictionaries. Compare it with the
explicit loop in main.py, including range(size). Do not rewrite or optimize it.
"""


def make_records(size):
    """Create the same unique synthetic ID records as the explicit version."""
    return [{"id": value} for value in range(size)]


"""
AI Explanation Prompt - Dictionary/list comprehensions and dict.get()
Explain the index construction and ordered query results below. Compare them
with indexed_lookup in main.py. Explain missing IDs, repeated queries, and
why unique record IDs matter. Do not rewrite or optimize the code.
"""


def indexed_lookup(records, queries):
    """Return equivalent answers and counts using compact index expressions."""
    index = {record["id"]: record for record in records}
    return [index.get(query) for query in queries], len(records), len(queries)


def main():
    """Reuse the experiment display with the compact equivalent functions."""
    explicit.run_demo(record_builder=make_records, lookup=indexed_lookup)


if __name__ == "__main__":
    main()
