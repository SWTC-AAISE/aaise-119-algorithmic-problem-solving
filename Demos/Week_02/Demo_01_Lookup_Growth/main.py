"""Recognize growth patterns with tiny, countable examples; no timing."""


def first_record(records):
    """Return the first record directly, or None for empty input."""
    if not records:
        return None
    return records[0]


def scan_lookup(records, queries):
    """Find the first match for each query and count inspected records."""
    results, inspected = [], 0
    for query in queries:
        found = None
        for record in records:
            inspected += 1
            if record["id"] == query:
                found = record
                break
        results.append(found)
    return results, inspected


def indexed_lookup(records, queries):
    """Build an ID index and return ordered answers plus setup/query counts."""
    index = {}
    for record in records:
        index[record["id"]] = record
    results = []
    for query in queries:
        if query in index:
            results.append(index[query])
        else:
            results.append(None)
    return results, len(records), len(queries)


def halving_trace(size):
    """Show repeated rounded-up halving for logarithmic growth intuition."""
    trace = []
    while size > 1:
        trace.append(size)
        size = (size + 1) // 2
    return trace + [size]


def make_records(size):
    """Create unique synthetic ID records using an explicit loop."""
    records = []
    for value in range(size):
        records.append({"id": value})
    return records


def run_demo(record_builder=make_records, lookup=indexed_lookup):
    """Illustrate growth shapes with small inputs rather than benchmark them."""
    print("GROWTH RECOGNITION: small equipment lookup examples")
    sample = record_builder(4)
    print("First equipment ID:", first_record(sample)["id"])
    print("Direct first-item access: O(1), regardless of collection size.")
    for size in (4, 8):
        _, count = scan_lookup(record_builder(size), [-1])
        print(f"One missing-ID scan through {size} records: {count} inspections -> O(n)")
    print("\nRepeated lookup: n queries through n records")
    print("Every query misses: count each inspected record, index entry, and query.")
    print(f"{'n':>6} {'q':>6} {'scan inspections':>18} {'index entries':>15} {'indexed queries':>17}")
    for size in (4, 8, 16):
        rows = record_builder(size)
        queries = [-1] * size
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
    """Run the explicit-loop version of the growth demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
