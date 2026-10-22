"""Fully commented companion to main.py: same experiment, every step explained.

This file is self-contained: it is ALL of main.py with full commenting.
The code behaves identically; the extra text is a reading aid that names the
growth shape of each function using Big-O notation, both letters and
description:

    O(1)     - "O of 1"         (Constant; best case of a first-match scan)
    O(n)     - "O of n"         (Linear; worst case of a first-match scan)
    O(n^2)   - "O of n squared" (Quadratic; repeated scans when q == n)
    O(q * n) - "O of q times n" (the general form behind that quadratic)

Big-O counts operations as the input grows; it ignores constants and hardware.
The legacy folder name says "Benchmark", but nothing here is timed: these are
tiny counted illustrations, not measurements.
"""


def make_records(size):
    """Create a small unique-ID fixture using explicit loops.

    Big-O: O(n) - "O of n" (Linear).
    One dictionary is appended per value in range(size), so the work grows
    in direct proportion to the requested size.
    """
    records = []
    # range(size) yields 0, 1, ..., size-1; each becomes a unique "id".
    for value in range(size):
        records.append({"id": value})
    return records


def find_record(records, target):
    """Return the first matching record or None, stopping at a match.

    Big-O: best case O(1) - "O of 1" (Constant) when the first record
    matches; worst case O(n) - "O of n" (Linear) when the target is last
    or missing. The shape depends on where the match sits, so a single
    scan has no one answer: ask "which case?" before naming a growth.
    """
    # Walk the records from the start, one at a time.
    for record in records:
        if record["id"] == target:
            return record  # First match wins; stop immediately.
    return None  # Target absent: every record was checked.


def scan_case(records, target):
    """Return a first-match answer and a small illustrative inspection count.

    Big-O: best case O(1) - "O of 1" (Constant); worst case O(n) -
    "O of n" (Linear). The returned count makes the case visible: 1
    inspection for a first-record hit, n inspections for a miss.
    """
    inspected = 0
    # Walk the records, counting each one we look at.
    for record in records:
        inspected += 1
        if record["id"] == target:
            return record, inspected  # Stop at the first match.
    return None, inspected  # A miss inspects all n records.


def run_demo(finder=find_record, record_builder=make_records):
    """Show case-dependent work and distinguish fixed queries from growing queries.

    Printed counts, not wall-clock timing, reveal the shapes:
    O(1) - "O of 1" (Constant) best case, O(n) - "O of n" (Linear) worst
    case, and O(n^2) - "O of n squared" (Quadratic) only when the number of
    queries grows together with the records.
    """
    print("CASE AND GROWTH RECOGNITION")
    records = record_builder(4)
    # Four positions of one scan: first, middle, last, and missing target.
    for label, target in (
        ("First match", 0),
        ("Middle match", 1),
        ("Last match", 3),
        ("Missing ID", -1),
    ):
        expected, inspections = scan_case(records, target)
        if finder(records, target) != expected:
            raise ValueError("The code forms disagree.")
        print(f"{label}: {inspections} record inspections")
    print("Best case: first match -> O(1). Worst case: last or missing -> O(n).")
    print(
        "Typical work depends on where requests match; it is not always the worst case."
    )
    print("\nWhen every query misses:")
    # Two fixed queries stay O(n); n queries become O(n^2).
    for size in (4, 8):
        _, per_query = scan_case(record_builder(size), -1)
        print(
            f"n={size}: 2 fixed queries -> {2 * per_query}; n queries -> {size * per_query}"
        )
    print("Fixed q: O(n). If q grows with n: O(n^2).")
    print(
        "A nested loop is not automatically quadratic: ask what each loop depends on."
    )
    print("These are tiny illustrations, not timed measurements or a benchmark.")


def main():
    """Run this fully commented version of the case-recognition demonstration."""
    run_demo()


if __name__ == "__main__":
    main()
