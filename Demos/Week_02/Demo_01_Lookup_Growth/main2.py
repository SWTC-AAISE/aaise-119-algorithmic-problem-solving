"""Fully commented companion to main.py: same experiment, every step explained.

This file is self-contained: it is ALL of main.py with full commenting.
The code behaves identically; the extra text is a reading aid that names the
growth shape of each function using Big-O notation, both letters and
description:

    O(1)     - "O of 1"         (Constant)
    O(log n) - "O of log n"     (Logarithmic)
    O(n)     - "O of n"         (Linear)
    O(q)     - "O of q"         (Linear in the number of queries)
    O(n + q) - "O of n plus q"  (Linear in the combined input sizes)
    O(n^2)   - "O of n squared" (Quadratic; the demo's scan_lookup shape)
    O(q * n) - "O of q times n" (the general form behind that quadratic)

Big-O counts operations as the input grows; it ignores constants and hardware.
"""


def first_record(records):
    """Return the first record directly, or None for empty input.

    Big-O: O(1) - "O of 1" (Constant).
    One emptiness check and at most one index access, no matter how many
    records exist. The work does not grow with the collection size.
    """
    # Guard: an empty list has no first element, so stop here.
    if not records:
        return None
    # Index 0 is a direct access; the cost is independent of len(records).
    return records[0]


def scan_lookup(records, queries):
    """Find the first match for each query and count inspected records.

    Big-O: O(n^2) - "O of n squared" (Quadratic) in this demo, where the
    number of queries equals the number of records (q == n): doubling n
    quadruples the worst-case number of inspections.

    Nuance: the function is really O(q * n) - "O of q times n" - q queries
    times up to n records each. A single query is only O(n) - "O of n"
    (Linear). It grows quadratically here because q grows together with n.
    """
    results, inspected = [], 0
    # Outer loop: one iteration per query (q iterations total).
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


def indexed_lookup(records, queries):
    """Build an ID index and return ordered answers plus setup/query counts.

    Big-O: O(n) - "O of n" (Linear) to build the dictionary index, then an
    expected average of O(1) - "O of 1" (Constant) per dictionary query, so
    O(q) - "O of q" (Linear) for all q queries. Total: O(n + q) -
    "O of n plus q" (Linear in the combined input sizes).
    Unique record IDs matter: a dictionary keeps one value per key, so a
    duplicate ID would silently overwrite an earlier record. Repeated queries
    are answered independently, in query order, and missing IDs answer None.
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
    return results, len(records), len(queries)


def halving_trace(size):
    """Show repeated rounded-up halving for logarithmic growth intuition.

    Big-O: O(log n) - "O of log n" (Logarithmic).
    Each step cuts the remaining size in half, so the number of steps grows
    with the logarithm of the starting size: 32 needs 5 halvings, and
    doubling the input adds only one extra step.
    """
    trace = []
    # Keep halving until only one element remains.
    while size > 1:
        trace.append(size)
        # (size + 1) // 2 rounds odd halves up, so the trace always shrinks.
        size = (size + 1) // 2
    return trace + [size]  # Append the final 1 to complete the trace.


def make_records(size):
    """Create unique synthetic ID records using an explicit loop.

    Big-O: O(n) - "O of n" (Linear).
    One dictionary is appended per value in range(size), so the work grows
    in direct proportion to the requested size.
    """
    records = []
    # range(size) yields 0, 1, ..., size-1; each becomes a unique "id".
    for value in range(size):
        records.append({"id": value})
    return records


def run_demo(record_builder=make_records, lookup=indexed_lookup):
    """Illustrate growth shapes with small inputs rather than benchmark them.

    Printed counts, not wall-clock timing, reveal the growth shapes:
    O(1) - "O of 1" (Constant) direct access, O(n) - "O of n" (Linear)
    single passes, O(n^2) - "O of n squared" (Quadratic) repeated scans when
    q == n, and O(log n) - "O of log n" (Logarithmic) halving.
    """
    print("GROWTH RECOGNITION: small equipment lookup examples")
    sample = record_builder(4)
    print("First equipment ID:", first_record(sample)["id"])
    print("Direct first-item access: O(1), regardless of collection size.")
    # A scan that misses must inspect every record: n inspections per query.
    for size in (4, 8):
        _, count = scan_lookup(record_builder(size), [-1])
        print(
            f"One missing-ID scan through {size} records: {count} inspections -> O(n)"
        )
    print("\nRepeated lookup: n queries through n records")
    print("Every query misses: count each inspected record, index entry, and query.")
    print(
        f"{'n':>6} {'q':>6} {'scan inspections':>18} {'index entries':>15} {'indexed queries':>17}"
    )
    for size in (4, 8, 16):
        rows = record_builder(size)
        queries = [-1] * size  # q == n here, so scan work grows quadratically.
        scan, inspections = scan_lookup(rows, queries)
        indexed, builds, lookups = lookup(rows, queries)
        if not (scan == indexed):
            raise ValueError("Cannot compare methods that return different results.")
        print(f"{size:>6} {size:>6} {inspections:>18} {builds:>15} {lookups:>17}")
    print("\nScan work is O(q*n); here q=n, so it grows quadratically.")
    print("Index construction is O(n); queries are expected average-case O(q).")
    print("An indexed query is an API-operation count, not a CPU instruction count.")
    print("Halving contrast:", halving_trace(32), "-> logarithmic number of reductions")
    print("Recognize the shape: direct access, one pass, repeated passes, or halving.")


def main():
    """Run this fully commented version of the growth demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
