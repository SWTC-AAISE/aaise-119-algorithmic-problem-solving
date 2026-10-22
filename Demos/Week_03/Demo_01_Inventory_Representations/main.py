"""Match equipment representations to lookup, update, and membership tasks."""

from console_style import print_color


def build_index(records):
    """Index independent flat record copies, rejecting duplicate equipment IDs."""
    index = {}
    for record in records:
        equipment_id = record["id"]
        if equipment_id in index:
            raise ValueError(f"duplicate ID: {equipment_id}")
        copied_record = record.copy()
        index[equipment_id] = copied_record
    return index


def scan_lookup(records, equipment_id):
    """Find one equipment record and report how many records were inspected."""
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == equipment_id:
            return record, inspected
    return None, inspected


def fixture():
    """Provide a small equipment inventory with a repeated equipment type."""
    return [
        {"id": "E01", "type": "laptop", "available": True},
        {"id": "E02", "type": "tablet", "available": True},
        {"id": "E03", "type": "laptop", "available": False},
    ]


def available_ids(index):
    """Collect the IDs of equipment currently available in the index."""
    # Original compact selection, kept as an optional reading comparison:
    # [key for key, row in index.items() if row["available"]]
    # items() supplies an ID and its record together. The loop below retrieves
    # that same record explicitly, checks availability, and collects the same ID.
    available = []
    for equipment_id in index:
        record = index[equipment_id]
        if record["available"]:
            available.append(equipment_id)
    return available


def display_record(record):
    """Present an equipment result without exposing dictionary notation."""
    if record is None:
        print_color("  No equipment found for that ID.", "caution")
        return
    if record["available"]:
        status = "Ready to borrow"
    else:
        status = "On loan"
    print(f"  {record['id']} - {record['type'].title()} - {status}")


def main():
    """Compare finding equipment, tracking unique types, and filtering availability."""
    rows = fixture()
    index = build_index(rows)
    # A set keeps each equipment type once, even when several records share it.
    types = {row["type"] for row in rows}

    print_color("EQUIPMENT LOAN DESK", "heading")
    print("Find equipment E03")
    found_record, inspected = scan_lookup(rows, "E03")
    print("List search:")
    display_record(found_record)
    print(f"  Records checked: {inspected}")
    print("ID index:")
    if "E03" in index:
        display_record(index["E03"])
    else:
        display_record(None)

    print_color("\nEquipment types we carry", "heading")
    for equipment_type in sorted(types):
        print(f"  {equipment_type.title()}")
    if "camera" in types:
        print("Camera requests: this type is in our inventory.")
    else:
        print("Camera requests: we do not carry this type.")

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
    for equipment_id in ready_ids:
        display_record(index[equipment_id])

    duplicate_rows = rows.copy()
    duplicate_record = rows[0].copy()
    duplicate_rows.append(duplicate_record)
    try:
        build_index(duplicate_rows)
    except ValueError:
        print_color("\nNew record not added: equipment ID E01 is already in use.", "caution")


if __name__ == "__main__":
    main()
