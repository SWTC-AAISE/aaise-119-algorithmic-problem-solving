"""Equipment loan demo with comments for combined filtering criteria.

This version keeps the original behavior of the demo while adding explanatory
documentation for classroom use. The main goal is to show the difference
between a behavior-preserving refactor and a real requirement change when more
than one condition controls selection.

The script highlights two related ideas:
1. Refactoring can improve readability without changing the answer.
2. Adding a new criterion, such as requiring a laptop, changes only part of the
   result while the rest of the loan rules remain stable.
"""

from console_style import color_text




# Shared inventory for both the report and the walkthrough.
EQUIPMENT = [
    {"id": "E01", "type": "laptop", "available": True, "battery": 80},
    {"id": "E02", "type": "tablet", "available": True, "battery": 50},
    {"id": "E03", "type": "laptop", "available": False, "battery": 90},
    {"id": "E04", "type": "laptop", "available": True, "battery": 50},
    {"id": "E05", "type": "laptop", "available": True, "battery": 49},
    {"id": "E06", "type": "laptop", "available": True, "battery": None},
]


def original_selection(records):
    """Apply the original inline rule used before refactoring.

    Args:
        records: A sequence of equipment dictionaries to inspect.

    Returns:
        list[dict]: Copies of records that match the original selection rule.
    """
    results = []
    for record in records:
        # This shows the original combined condition before it is named.
        if valid_record(record) and record["available"] and record["battery"] >= 50:
            results.append(record.copy())
    return results


def valid_record(record):
    """Check whether a record is safe to use in the loan rules.

    Args:
        record: A dictionary describing one equipment item.

    Returns:
        bool: True when the record contains trusted values for all required
        fields, otherwise False.
    """
    # Validation happens first so later rule checks do not depend on bad data.
    return (
        isinstance(record.get("id"), str)
        and bool(record["id"].strip())
        and record.get("type") in ("laptop", "tablet")
        and type(record.get("available")) is bool
        and type(record.get("battery")) is int
        and 0 <= record["battery"] <= 100
    )


def ready_for_loan(record):
    """Decide whether a device meets the original readiness rules.

    Args:
        record: A dictionary describing one equipment item.

    Returns:
        bool: True when the equipment is valid, available, and has at least 50%
        battery.
    """
    # This named helper preserves the original rule but makes it reusable.
    return valid_record(record) and record["available"] and record["battery"] >= 50


def matches_laptop_request(record):
    """Apply the revised request that requires a laptop specifically.

    Args:
        record: A dictionary describing one equipment item.

    Returns:
        bool: True when the equipment is ready for loan and is a laptop.
    """
    # The new requirement adds one more condition without changing the others.
    return ready_for_loan(record) and record["type"] == "laptop"


def select_equipment(records, rule):
    """Collect copies of records that satisfy a supplied rule.

    Args:
        records: A sequence of equipment dictionaries to inspect.
        rule: A function that returns True for records that should be selected.

    Returns:
        list[dict]: Copies of matching records in their original order.
    """
    selected = []
    for record in records:
        if rule(record):
            selected.append(record.copy())
    return selected


def ids(records):
    """Extract record identifiers for compact walkthrough evidence.

    Args:
        records: A sequence of selected equipment dictionaries.

    Returns:
        list[str]: The IDs from the supplied records, in order.
    """
    # Short ID lists make before-and-after comparisons easier to read.
    return [row["id"] for row in records]


def show_report(records=EQUIPMENT):
    """Print the user-facing report for the revised laptop request.

    Args:
        records: A sequence of equipment dictionaries to include in the report.

    Returns:
        None: This function prints the final report.
    """
    # The normal report uses only the revised laptop-specific rule.
    selected = select_equipment(records, matches_laptop_request)

    print(color_text("Equipment Loan Desk - Laptop Class Request", "heading"))
    print("Request: Available laptops with at least 50% battery\n")
    print(color_text("Ready to borrow", "success"))

    for record in selected:
        print(
            color_text(
                f"  {record['id']} - Laptop - Battery {record['battery']}%",
                "success",
            )
        )

    if not selected:
        print(color_text("  No laptops meet this request.", "caution"))

    # Build explanations for everything excluded so the decision remains visible.
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
            print(
                color_text(
                    f"  {record.get('id') or 'Unidentified equipment'} - {reason}",
                    "caution",
                )
            )

    print(f"\nResult: {len(selected)} laptop(s) ready for class.")


def continue_walkthrough(pause):
    """Pause between walkthrough steps when requested.

    Args:
        pause: True to wait for Enter between steps, False to continue without
        stopping.

    Returns:
        bool: True when the walkthrough should continue, otherwise False.
    """
    if not pause:
        return True
    try:
        input("\nPress Enter for the next step...")
    except (EOFError, KeyboardInterrupt):
        # Handle interrupted input as a graceful stop instead of a crash.
        print("\nWalkthrough stopped.")
        return False
    return True


def show_walkthrough(pause=True):
    """Explain refactoring versus a genuine change in selection criteria.

    Args:
        pause: True to pause between teaching steps, False to run through.

    Returns:
        None: This function prints the guided walkthrough.
    """
    print(color_text("1. Original Request", "heading"))
    print("Any valid available device with at least 50% battery qualifies.")
    print("Predict E02 (tablet, 50%) and E04 (laptop, 50%).")
    if not continue_walkthrough(pause):
        return

    print(color_text("\n2. Refactor Without Changing the Answer", "heading"))
    print("English: The device must be valid, available, and charged to at least 50%.")
    print("Pseudocode: for each device, if ready_for_loan passes, collect it.")
    print(color_text("def ready_for_loan(record):", "code"))
    print(
        color_text(
            '    """Recognize trusted equipment available with at least 50% battery."""',
            "code",
        )
    )
    print(
        color_text(
            "    return valid_record(record) and record['available'] and record['battery'] >= 50",
            "code",
        )
    )
    print(
        "A named function supplies the rule; the collector owns the loop. No lambda needed."
    )

    # Compare the original inline code with the refactored helper-based version.
    print("Expected before AND after refactor: E01, E02, E04")
    print("Actual original:", ", ".join(ids(original_selection(EQUIPMENT))))
    print(
        "Actual refactor:", ", ".join(ids(select_equipment(EQUIPMENT, ready_for_loan)))
    )
    if not continue_walkthrough(pause):
        return

    print(color_text("\n3. Changed Requirement", "heading"))
    print(
        "This class now needs laptops. Keep availability and the 50% boundary unchanged."
    )
    print("English: ready for loan AND a laptop.")
    print(
        color_text(
            "return ready_for_loan(record) and record['type'] == 'laptop'", "code"
        )
    )
    print("Predict which answer changes and which answers must remain unchanged.")
    if not continue_walkthrough(pause):
        return

    print(color_text("\n4. Changed and Preserved Expectations", "heading"))
    print(f"{'Device':<10} {'Original':<12} {'Revised':<12} Match?")

    # Each tuple states the expected result before and after the new criterion.
    expected = [
        (True, True),
        (True, False),
        (False, False),
        (True, True),
        (False, False),
        (False, False),
    ]
    for record, (before, after) in zip(EQUIPMENT, expected):
        actual_before = ready_for_loan(record)
        actual_after = matches_laptop_request(record)
        match = actual_before == before and actual_after == after
        print(
            f"{record['id']:<10} {'Ready' if actual_before else 'Not ready':<12} "
            f"{'Ready' if actual_after else 'Not ready':<12} "
            + color_text("Yes" if match else "No", "success" if match else "failure")
        )

    print("Expected: only E02 changes. E04 still qualifies at exactly 50%.")
    print("On-loan, undercharged, and unknown readings remain excluded.")
    if not continue_walkthrough(pause):
        return

    print(color_text("\n5. The Useful Answer", "heading"))
    show_report()


def main():
    """Run the menu for the report, walkthrough, or exit.

    Returns:
        None: This function manages the demo until the user exits.
    """
    while True:
        print(color_text("\nEquipment Loan Desk - Combined Criteria Demo", "heading"))
        print("1. View the laptop report\n2. Explore the teaching walkthrough\n0. Exit")
        try:
            choice = input("Choose 1, 2, or 0: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return

        # Keep each menu option mapped to one clear behavior.
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
