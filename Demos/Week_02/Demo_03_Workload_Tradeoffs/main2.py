"""Fully commented companion to main.py: same experiment, every step explained.

This file is self-contained: it is ALL of main.py with full commenting.
The code behaves identically; the extra text is a reading aid that names the
growth shape of each function using Big-O notation, both letters and
description:

    O(1)     - "O of 1"         (Constant; average existing-index lookup)
    O(n)     - "O of n"         (Linear; index build or one scan pass)
    O(n^2)   - "O of n squared" (Quadratic; repeated scans when q == n)
    O(q * n) - "O of q times n" (the general form behind that quadratic)

Big-O counts operations as the input grows; it ignores constants and hardware.
Storage has a shape too: the dictionary index costs O(n) - "O of n" (Linear)
extra space, which is the tradeoff this demonstration discusses.
"""


def make_records(size):
    """Create a small unique-ID equipment fixture.

    Big-O: O(n) - "O of n" (Linear).
    One dictionary is appended per value in range(size), so the work grows
    in direct proportion to the requested size.
    """
    records = []
    # range(size) yields 0, 1, ..., size-1; each becomes a unique "id".
    for value in range(size):
        records.append({"id": value})
    return records


def scan(records, queries):
    """Collect first-match answers and small illustrative record counts.

    Big-O: O(n^2) - "O of n squared" (Quadratic) when the number of
    queries grows with the records (q == n): doubling n quadruples the
    worst-case number of inspections.

    Nuance: the function is really O(q * n) - "O of q times n" - q queries
    times up to n records each. A single query is only O(n) - "O of n"
    (Linear), and an early hit can stop after O(1) - "O of 1" inspections.
    """
    results = []
    inspected = 0
    # Outer loop: one iteration per query.
    for query in queries:
        found = None
        # Inner loop: walk records from the start until the first match.
        for record in records:
            inspected += 1  # Count every record we look at.
            if record["id"] == query:
                found = record
                break  # First match wins; stop scanning this query early.
        # Record the match (or None when the query ID was absent).
        results.append(found)
    return results, inspected


def indexed(records, queries):
    """Build a unique-ID dictionary and collect ordered answers.

    Big-O: O(n) - "O of n" (Linear) to build the dictionary index, then an
    expected average of O(1) - "O of 1" (Constant) per key lookup, so
    O(q) - "O of q" (Linear) for all q queries. Total: O(n + q) -
    "O of n plus q" (Linear in the combined input sizes).
    Storage tradeoff: the index itself costs O(n) - "O of n" (Linear) extra
    space and must be updated when records change. Unique IDs matter: a
    dictionary keeps one value per key, so a duplicate ID would silently
    overwrite an earlier record.
    """
    index = {}
    # One pass over the records: each ID becomes a key pointing at its record.
    for record in records:
        index[record["id"]] = record
    results = []
    # One dictionary probe per query; membership and access are each
    # expected average-case O(1) - "O of 1" (Constant).
    for query in queries:
        if query in index:
            results.append(index[query])
        else:
            results.append(None)  # Missing IDs answer None, in query order.
    return results


def run_demo(index_function=indexed, record_builder=make_records):
    """Contrast a one-off request and repeated lookups without measuring speed.

    The counted operations reveal the shapes: a one-off early hit needs no
    index at all, while repeated requests can justify an O(n) - "O of n"
    (Linear) build that pays back with average O(1) - "O of 1" (Constant)
    lookups. Counted work is not a measured speed winner.
    """
    print("WORKLOAD RECOGNITION: four equipment records")
    records = record_builder(4)
    # Two request patterns: a single early hit, then a repeated mixed batch.
    for label, queries in (
        ("One early hit", [0]),
        ("Repeated mixed requests", [0, 3, -1] * 2),
    ):
        answers, inspections = scan(records, queries)
        if answers != index_function(records, queries):
            raise ValueError("Lookup results disagree.")
        print(f"\n{label}: {len(queries)} request(s)")
        print(f"Scan: {inspections} illustrative record inspections")
        print(f"Index: build {len(records)} entries; make {len(queries)} key lookup(s)")
    print("\nOne early hit can be served without building an index.")
    print("Repeated ID lookups may justify building and retaining an index.")
    print("Building the index is O(n); one existing-index lookup is average-case O(1).")
    print("The index requires additional storage and must reflect record changes.")
    print("Different counted operations do not establish a measured speed winner.")
    print("Choose for the request and reuse pattern, not a universal 'fastest' claim.")


def main():
    """Run this fully commented version of the workload demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
