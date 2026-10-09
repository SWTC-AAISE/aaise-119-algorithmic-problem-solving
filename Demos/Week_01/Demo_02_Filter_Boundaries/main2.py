"""Equipment Loan Desk boundary demo with teaching comments.

This version of the app keeps the original behavior but adds explanatory
documentation for classroom use. The main goal is to show how a small boundary
decision, such as using `>` instead of `>=`, changes which equipment qualifies
for lending when the battery is exactly at the minimum threshold.

The script supports two related outcomes:
1. Compare an intentional boundary bug with the corrected rule.
2. Produce a practical equipment loan report using the corrected rule.
"""

from console_style import color_text




def valid_record(record):
    """Check that a record has trustworthy availability and battery data.

    Args:
        record: A dictionary describing one equipment item.

    Returns:
        bool: True when the record contains a Boolean availability flag and an
        integer battery percentage from 0 through 100.
    """
    # Validate types first so later numeric comparisons remain safe.
    return (
        type(record.get("available")) is bool
        and type(record.get("battery")) is int
        and 0 <= record["battery"] <= 100
    )


def buggy_predicate(record, threshold):
    """Apply the intentionally incorrect boundary rule for demonstration.

    Args:
        record: A dictionary describing one equipment item.
        threshold: The minimum battery percentage required for lending.

    Returns:
        bool: True when the item passes the buggy rule, otherwise False.
    """
    # Keep the defect explicit so students can isolate the wrong comparison.
    return (
        valid_record(record) and record["available"] and record["battery"] > threshold
    )


def corrected_predicate(record, threshold):
    """Apply the corrected boundary rule used by the real loan decision.

    Args:
        record: A dictionary describing one equipment item.
        threshold: The minimum battery percentage required for lending.

    Returns:
        bool: True when the item is valid, available, and at or above the
        threshold.
    """
    # The corrected rule includes the exact threshold as acceptable.
    return (
        valid_record(record) and record["available"] and record["battery"] >= threshold
    )


# These cases deliberately cover below, exact, above, and invalid inputs.
CASES = [
    ("below", {"available": True, "battery": 49}, False),
    ("exact boundary", {"available": True, "battery": 50}, True),
    ("above", {"available": True, "battery": 51}, True),
    ("unavailable", {"available": False, "battery": 90}, False),
    ("missing battery", {"available": True}, False),
    ("unknown battery", {"available": True, "battery": None}, False),
    ("out of range", {"available": True, "battery": 101}, False),
]


def show_comparisons(predicate):
    """Print expected versus actual outcomes for a selected rule.

    Args:
        predicate: The decision function to evaluate against each sample case.

    Returns:
        None: This function prints a comparison table.
    """
    # Use one shared threshold so each example targets the same rule boundary.
    print(f"\n{'Situation':<20} {'Expected':<12} {'Actual':<12} Match?")
    for label, record, expected in CASES:
        actual = predicate(record, 50)
        match = actual == expected

        # Show the mismatch clearly so the boundary defect is easy to spot.
        print(
            f"{label:<20} {'Ready' if expected else 'Not ready':<12} "
            f"{'Ready' if actual else 'Not ready':<12} "
            + color_text("Yes" if match else "No", "success" if match else "failure")
        )


# Add simple IDs so the report can refer to each sample like real inventory.
EQUIPMENT = [
    dict(record, id=f"E{index:02}") for index, (_, record, _) in enumerate(CASES, 1)
]


def select_equipment(records, threshold=50):
    """Split records into ready items and excluded items with reasons.

    Args:
        records: A sequence of equipment dictionaries to evaluate.
        threshold: The minimum battery percentage required for lending.

    Returns:
        tuple[list[dict], list[tuple[dict, str]]]: Ready equipment and excluded
        equipment paired with a reason.

    Raises:
        ValueError: If the threshold is not an integer from 0 through 100.
    """
    # Validate the threshold up front so every later comparison is meaningful.
    if type(threshold) is not int or not 0 <= threshold <= 100:
        raise ValueError("Battery minimum must be an integer from 0 through 100.")

    # Keep successful and excluded records separate for a clearer final report.
    selected, excluded = [], []
    for record in records:
        if not valid_record(record):
            reason = "Battery or availability details need checking before lending"
        elif not record["available"]:
            reason = "Already on loan"
        elif not corrected_predicate(record, threshold):
            reason = "Charge before lending"
        else:
            selected.append(record.copy())
            continue

        # Copy excluded records so later changes do not mutate the report data.
        excluded.append((record.copy(), reason))
    return selected, excluded


def show_report(records=EQUIPMENT):
    """Display a user-facing classroom loan report.

    Args:
        records: A sequence of equipment dictionaries to include in the report.

    Returns:
        None: This function prints the loan report.
    """
    # Reuse the selection logic so the report matches the actual rule.
    selected, excluded = select_equipment(records)

    print(color_text("Equipment Loan Desk - Classroom Loan List", "heading"))
    print("Request: Available equipment with at least 50% battery\n")

    # Show ready items first because that is the main answer a borrower needs.
    print(color_text("Ready to borrow", "success"))
    for record in selected:
        print(color_text(f"  {record['id']} - Battery {record['battery']}%", "success"))

    if not selected:
        print(color_text("  No equipment meets this request.", "caution"))

    # After the ready list, explain what was left out and why.
    if excluded:
        print(color_text("\nNot included", "caution"))
        for record, reason in excluded:
            print(
                color_text(
                    f"  {record.get('id') or 'Unidentified equipment'} - {reason}",
                    "caution",
                )
            )

    print(f"\nResult: {len(selected)} equipment item(s) ready to borrow.")


def continue_walkthrough(pause):
    """Pause between walkthrough steps unless pausing is disabled.

    Args:
        pause: True to wait for Enter between steps, False to continue without
        stopping.

    Returns:
        bool: True when the walkthrough should continue, otherwise False.
    """
    # Allow automated runs or quick demos to skip interactive pauses.
    if not pause:
        return True

    try:
        input("\nPress Enter for the next step...")
    except (EOFError, KeyboardInterrupt):
        # Treat interrupted input as a graceful stop rather than a crash.
        print("\nWalkthrough stopped.")
        return False
    return True


def show_walkthrough(pause=True):
    """Guide the user through the problem, the bug, and the repair.

    Args:
        pause: True to wait between steps, False to run straight through.

    Returns:
        None: This function prints the teaching walkthrough.
    """
    # Store the lesson as ordered steps so the classroom flow stays consistent.
    steps = [
        (
            "1. Problem and Precise Rule",
            "The desk needs available equipment with at least 50% battery.\nExactly 50% qualifies; unknown readings need checking. Predict 49%, 50%, and 51%.",
        ),
        (
            "2. Representation Bridge",
            "English: Trust the details, then require availability AND battery at least 50%.\nPseudocode: if valid AND available AND battery >= minimum: include equipment",
        ),
        (
            "3. Deliberately Incorrect Rule",
            "Teaching only: battery > minimum. The normal report never uses this defect.",
        ),
        (
            "4. Repair and Regression",
            "Change > to >=. Only the boundary answer should change.",
        ),
        (
            "5. The Useful Answer",
            "Apply the corrected rule to the classroom loan inventory.",
        ),
    ]

    for index, (heading, explanation) in enumerate(steps):
        print(color_text("\n" + heading, "heading"))
        print(explanation)

        # Inject the right artifact at the right step so the lesson builds in order.
        if index == 1:
            print(
                color_text(
                    "return valid_record(record) and record['available'] and record['battery'] >= threshold",
                    "code",
                )
            )
            print(
                "Validation comes first so unknown readings are not compared with numbers."
            )
        elif index == 2:
            show_comparisons(buggy_predicate)
            print("The above-threshold happy path cannot reveal the boundary defect.")
        elif index == 3:
            show_comparisons(corrected_predicate)
            print(
                "Unavailable and invalid items remain excluded. More checks are in test_demo.py."
            )
        elif index == 4:
            show_report()

        # Stop cleanly if the user ends the walkthrough between steps.
        if index < 4 and not continue_walkthrough(pause):
            return


def main():
    """Run the menu that exposes the report and the guided walkthrough.

    Returns:
        None: This function manages user interaction until exit.
    """
    # Keep the interface small so the learning focus stays on the decision rule.
    while True:
        print(color_text("\nEquipment Loan Desk - Boundary Demo", "heading"))
        print("1. View the loan list\n2. Explore the teaching walkthrough\n0. Exit")

        try:
            choice = input("Choose 1, 2, or 0: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return

        # Route each choice to one clear behavior and reject anything else.
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
