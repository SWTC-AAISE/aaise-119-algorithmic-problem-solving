"""Discuss lookup choices using tiny traces and qualitative storage tradeoffs."""


def make_records(size):
    """Create a small unique-ID equipment fixture."""
    records = []
    for value in range(size):
        records.append({"id": value})
    return records


def scan(records, queries):
    """Collect first-match answers and small illustrative record counts."""
    results = []
    inspected = 0
    for query in queries:
        found = None
        for record in records:
            inspected += 1
            if record["id"] == query:
                found = record
                break
        results.append(found)
    return results, inspected


def indexed(records, queries):
    """Build a unique-ID dictionary and collect ordered answers."""
    index = {}
    for record in records:
        index[record["id"]] = record
    results = []
    for query in queries:
        if query in index:
            results.append(index[query])
        else:
            results.append(None)
    return results


def run_demo(index_function=indexed, record_builder=make_records):
    """Contrast a one-off request and repeated lookups without measuring speed."""
    print("WORKLOAD RECOGNITION: four equipment records")
    records = record_builder(4)
    for label, queries in (("One early hit", [0]), ("Repeated mixed requests", [0, 3, -1] * 2)):
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
    """Run the explicit-loop qualitative workload demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
