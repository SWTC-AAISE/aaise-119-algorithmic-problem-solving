"""Recognize scan cases and growth; the legacy folder name is not a benchmark."""

def make_records(size):
    """Create a small unique-ID fixture using explicit loops."""
    records = []
    for value in range(size):
        records.append({"id": value})
    return records


def find_record(records, target):
    """Return the first matching record or None, stopping at a match."""
    for record in records:
        if record["id"] == target:
            return record
    return None


def scan_case(records, target):
    """Return a first-match answer and a small illustrative inspection count."""
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == target:
            return record, inspected
    return None, inspected


def run_demo(finder=find_record, record_builder=make_records):
    """Show case-dependent work and distinguish fixed queries from growing queries."""
    print("CASE AND GROWTH RECOGNITION")
    records = record_builder(4)
    for label, target in (("First match", 0), ("Middle match", 1),
                          ("Last match", 3), ("Missing ID", -1)):
        expected, inspections = scan_case(records, target)
        if finder(records, target) != expected:
            raise ValueError("The code forms disagree.")
        print(f"{label}: {inspections} record inspections")
    print("Best case: first match -> O(1). Worst case: last or missing -> O(n).")
    print("Typical work depends on where requests match; it is not always the worst case.")
    print("\nWhen every query misses:")
    for size in (4, 8):
        _, per_query = scan_case(record_builder(size), -1)
        print(f"n={size}: 2 fixed queries -> {2 * per_query}; n queries -> {size * per_query}")
    print("Fixed q: O(n). If q grows with n: O(n^2).")
    print("A nested loop is not automatically quadratic: ask what each loop depends on.")
    print("These are tiny illustrations, not timed measurements or a benchmark.")


def main():
    """Run the explicit-loop case-recognition demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
