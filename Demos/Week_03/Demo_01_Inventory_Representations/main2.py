"""Documented companion to main.py; the executable behavior is unchanged.

Monday's lecture asks which structure makes a particular operation clear.
This equipment desk uses a list for sequence, an ID dictionary for lookup,
and a set for distinct type names. The comments explain the decisions behind
those choices, especially identity, membership, filtering, and flat record copies.
Read main.py when you want to see the code without the extra teaching detail.
"""

# Presentation is separate from the algorithms. This helper adds readable color;
# it does not decide which equipment exists or is available.
from console_style import print_color


def build_index(records):
    """Index independent flat record copies, rejecting duplicate equipment IDs.

    Args:
        records: Equipment dictionaries containing id, type, and available.

    Returns:
        A dictionary connecting each equipment ID to its copied record.

    Raises:
        ValueError: When two records claim the same equipment ID.
    """
    index = {}
    for record in records:
        # Identity comes from the record's ID, not its current list position.
        equipment_id = record["id"]
        # Dictionary membership checks keys. Without this guard, assigning the
        # same key again would silently replace its earlier record.
        if equipment_id in index:
            raise ValueError(f"duplicate ID: {equipment_id}")
        # Indexing alone does not copy records. We deliberately copy this flat
        # dictionary so a working availability edit leaves the supplied row alone.
        # Its values are strings/Booleans; nested-copy mechanics are not needed.
        copied_record = record.copy()
        index[equipment_id] = copied_record
    return index


def scan_lookup(records, equipment_id):
    """Find one record and return (matching record or None, inspections).

    A first match stops the scan. A missing ID requires visiting the whole list.
    The count illustrates that pattern; it is not a timing measurement.
    """
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == equipment_id:
            # Return both answers together; the caller gives each a separate name.
            return record, inspected
    # None means not found, not an invalid dictionary. This return belongs after
    # the loop so the search does not give up after just one nonmatching row.
    return None, inspected


def fixture():
    """Create three records whose IDs, repeated types, and statuses serve different jobs."""
    # E01 and E03 share a TYPE but not an ID. Collapsing repeated type names is
    # useful; collapsing equipment records with distinct IDs would lose inventory.
    return [
        {"id": "E01", "type": "laptop", "available": True},
        {"id": "E02", "type": "tablet", "available": True},
        {"id": "E03", "type": "laptop", "available": False},
    ]


def available_ids(index):
    """Return the IDs of available records, retaining registry iteration order.

    This is filtering, not direct lookup: an index keyed by ID does not directly
    answer a question about every record's availability. Visit the records.
    """
    # Optional compact equivalent, not a syntax requirement:
    # [key for key, row in index.items() if row["available"]]
    # items() supplies each key and record together. Below we name the key first,
    # then retrieve its record explicitly; the selection rule is the same.
    available = []
    for equipment_id in index:
        record = index[equipment_id]
        if record["available"]:
            available.append(equipment_id)
    # These results are ID strings, not copied records. AL03's category-report
    # contract requires the additional copied-record step taught in the lecture.
    return available


def display_record(record):
    """Present a found or missing result in the loan desk user's language."""
    if record is None:
        print_color("  No equipment found for that ID.", "caution")
        return
    # The stored Boolean is useful for decisions. The reader sees its meaning,
    # not a raw dictionary dump or an unexplained True/False value.
    if record["available"]:
        status = "Ready to borrow"
    else:
        status = "On loan"
    # .title() makes the type label presentable without changing the record.
    print(f"  {record['id']} - {record['type'].title()} - {status}")


def main():
    """Compare lookup, unique types, independent edits, and availability filtering."""
    rows = fixture()
    index = build_index(rows)
    # Set comprehension: produce row['type'] for every row, retaining each
    # distinct value once. The explicit form taught first in the lecture is:
    # types = set()
    # for row in rows:
    #     types.add(row["type"])
    # The three records therefore produce two types: laptop and tablet.
    types = {row["type"] for row in rows}

    print_color("EQUIPMENT LOAN DESK", "heading")
    print("Find equipment E03")
    # Unpack the scan's two results into meaningful names. E03 is a valid match
    # even though it is on loan: finding identity is not availability filtering.
    found_record, inspected = scan_lookup(rows, "E03")
    print("List search:")
    display_record(found_record)
    print(f"  Records checked: {inspected}")
    print("ID index:")
    # Query an index already built above. Its setup still visited all records;
    # expected average-case O(1) describes this key lookup, not build plus query.
    if "E03" in index:
        display_record(index["E03"])
    else:
        display_record(None)

    print_color("\nEquipment types we carry", "heading")
    # Sets do not guarantee display order. sorted() supplies a sorted list for
    # this report; it does not turn the original set into an ordered set.
    for equipment_type in sorted(types):
        print(f"  {equipment_type.title()}")
    # Membership returns a yes/no answer, not a position or equipment record.
    # This set describes OBSERVED types; AL03's supported categories are a
    # separately supplied vocabulary that may include currently empty categories.
    if "camera" in types:
        print("Camera requests: this type is in our inventory.")
    else:
        print("Camera requests: we do not carry this type.")

    # First brackets find E01's record; second brackets select its mutable field.
    index["E01"]["available"] = False
    print_color("\nAfter checking out E01 in the working index", "heading")
    print("Working record:")
    display_record(index["E01"])
    print("Original record, kept separately:")
    display_record(rows[0])
    print("  This index uses flat copies; Week 2's index shared its records.")

    print_color("\nReady to borrow now", "heading")
    ready_ids = available_ids(index)
    if not ready_ids:
        print("  No equipment is ready to borrow.")
    # E01 was just checked out and E03 was already on loan: only E02 qualifies.
    for equipment_id in ready_ids:
        display_record(index[equipment_id])

    # Build a separate duplicate attempt so the original fixture stays unchanged.
    # rows.copy() copies the outer list only. Copying the selected record too
    # gives the appended example its own dictionary; it still has the SAME ID.
    duplicate_rows = rows.copy()
    duplicate_record = rows[0].copy()
    duplicate_rows.append(duplicate_record)
    try:
        build_index(duplicate_rows)
    except ValueError:
        # Convert the technical rejection into a useful user-facing message.
        print_color("\nNew record not added: equipment ID E01 is already in use.", "caution")


# Importing this file exposes its functions without automatically running the app.
if __name__ == "__main__":
    main()
