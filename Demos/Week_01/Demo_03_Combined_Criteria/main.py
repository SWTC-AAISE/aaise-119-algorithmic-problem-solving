"""Separate behavior-preserving refactoring from a changed filter requirement."""

from console_style import color_text




EQUIPMENT = [
    {"id": "E01", "type": "laptop", "available": True, "battery": 80},
    {"id": "E02", "type": "tablet", "available": True, "battery": 50},
    {"id": "E03", "type": "laptop", "available": False, "battery": 90},
    {"id": "E04", "type": "laptop", "available": True, "battery": 50},
    {"id": "E05", "type": "laptop", "available": True, "battery": 49},
    {"id": "E06", "type": "laptop", "available": True, "battery": None},
]


def original_selection(records):
    """Select ready devices using the original inline loan conditions."""
    results = []
    for record in records:
        if valid_record(record) and record["available"] and record["battery"] >= 50:
            results.append(record.copy())
    return results


def valid_record(record):
    """Check equipment details before trusting any loan rule."""
    return (isinstance(record.get("id"), str) and bool(record["id"].strip())
            and record.get("type") in ("laptop", "tablet")
            and type(record.get("available")) is bool
            and type(record.get("battery")) is int and 0 <= record["battery"] <= 100)


def ready_for_loan(record):
    """Recognize trusted equipment available with at least 50% battery."""
    return valid_record(record) and record["available"] and record["battery"] >= 50


def matches_laptop_request(record):
    """Apply the revised request for a ready laptop rather than any device."""
    return ready_for_loan(record) and record["type"] == "laptop"


def select_equipment(records, rule):
    """Collect matching copies in inventory order using one named rule."""
    selected = []
    for record in records:
        if rule(record):
            selected.append(record.copy())
    return selected


def ids(records):
    """Extract identifiers for compact teaching evidence, not the normal report."""
    return [row["id"] for row in records]


def show_report(records=EQUIPMENT):
    """Show ready laptops and useful actions for equipment not included."""
    selected = select_equipment(records, matches_laptop_request)
    print(color_text("Equipment Loan Desk - Laptop Class Request", "heading"))
    print("Request: Available laptops with at least 50% battery\n")
    print(color_text("Ready to borrow", "success"))
    for record in selected:
        print(color_text(f"  {record['id']} - Laptop - Battery {record['battery']}%", "success"))
    if not selected:
        print(color_text("  No laptops meet this request.", "caution"))
    excluded = [record for record in records if not matches_laptop_request(record)]
    if excluded:
        print(color_text("\nNot included", "caution"))
        for record in excluded:
            if not valid_record(record):
                reason = "Equipment details need checking before lending"
            elif record["type"] != "laptop":
                reason = "Tablet available, but this class needs a laptop"
            elif not record["available"]:
                reason = "Already on loan"
            else:
                reason = "Charge before lending"
            print(color_text(f"  {record.get('id') or 'Unidentified equipment'} - {reason}", "caution"))
    print(f"\nResult: {len(selected)} laptop(s) ready for class.")


def continue_walkthrough(pause):
    """Allow predictions before the next reveal and handle interrupted input."""
    if not pause:
        return True
    try:
        input("\nPress Enter for the next step...")
    except (EOFError, KeyboardInterrupt):
        print("\nWalkthrough stopped.")
        return False
    return True


def show_walkthrough(pause=True):
    """Distinguish a behavior-preserving refactor from a changed loan request."""
    print(color_text("1. Original Request", "heading"))
    print("Any valid available device with at least 50% battery qualifies.")
    print("Predict E02 (tablet, 50%) and E04 (laptop, 50%).")
    if not continue_walkthrough(pause):
        return
    print(color_text("\n2. Refactor Without Changing the Answer", "heading"))
    print("English: The device must be valid, available, and charged to at least 50%.")
    print("Pseudocode: for each device, if ready_for_loan passes, collect it.")
    print(color_text("def ready_for_loan(record):", "code"))
    print(color_text('    """Recognize trusted equipment available with at least 50% battery."""', "code"))
    print(color_text("    return valid_record(record) and record['available'] and record['battery'] >= 50", "code"))
    print("A named function supplies the rule; the collector owns the loop. No lambda needed.")
    print("Expected before AND after refactor: E01, E02, E04")
    print("Actual original:", ", ".join(ids(original_selection(EQUIPMENT))))
    print("Actual refactor:", ", ".join(ids(select_equipment(EQUIPMENT, ready_for_loan))))
    if not continue_walkthrough(pause):
        return
    print(color_text("\n3. Changed Requirement", "heading"))
    print("This class now needs laptops. Keep availability and the 50% boundary unchanged.")
    print("English: ready for loan AND a laptop.")
    print(color_text("return ready_for_loan(record) and record['type'] == 'laptop'", "code"))
    print("Predict which answer changes and which answers must remain unchanged.")
    if not continue_walkthrough(pause):
        return
    print(color_text("\n4. Changed and Preserved Expectations", "heading"))
    print(f"{'Device':<10} {'Original':<12} {'Revised':<12} Match?")
    expected = [(True, True), (True, False), (False, False),
                (True, True), (False, False), (False, False)]
    for record, (before, after) in zip(EQUIPMENT, expected):
        actual_before, actual_after = ready_for_loan(record), matches_laptop_request(record)
        match = actual_before == before and actual_after == after
        print(f"{record['id']:<10} {'Ready' if actual_before else 'Not ready':<12} "
              f"{'Ready' if actual_after else 'Not ready':<12} "
              + color_text("Yes" if match else "No", "success" if match else "failure"))
    print("Expected: only E02 changes. E04 still qualifies at exactly 50%.")
    print("On-loan, undercharged, and unknown readings remain excluded.")
    if not continue_walkthrough(pause):
        return
    print(color_text("\n5. The Useful Answer", "heading"))
    show_report()


def main():
    """Offer the useful laptop report separately from teaching evidence."""
    while True:
        print(color_text("\nEquipment Loan Desk - Combined Criteria Demo", "heading"))
        print("1. View the laptop report\n2. Explore the teaching walkthrough\n0. Exit")
        try:
            choice = input("Choose 1, 2, or 0: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return
        if choice == "1":
            show_report()
        elif choice == "2":
            show_walkthrough()
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print(color_text("Please choose 1, 2, or 0.", "caution"))


if __name__ == "__main__":
    main()
