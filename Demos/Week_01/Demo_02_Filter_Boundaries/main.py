"""Preserve a deliberate boundary bug and compare it with a corrected rule."""


from console_style import color_text




def valid_record(record):
    """Check availability and battery details before trusting a loan decision."""
    return (type(record.get("available")) is bool
            and type(record.get("battery")) is int
            and 0 <= record["battery"] <= 100)


def buggy_predicate(record, threshold):
    """Expose the intentional boundary defect only for teaching."""
    # Deliberate teaching defect: the contract includes the exact threshold.
    return valid_record(record) and record["available"] and record["battery"] > threshold


def corrected_predicate(record, threshold):
    """Accept trusted available equipment at or above the battery minimum."""
    return valid_record(record) and record["available"] and record["battery"] >= threshold


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
    """Compare independently stated expectations with the chosen teaching rule."""
    print(f"\n{'Situation':<20} {'Expected':<12} {'Actual':<12} Match?")
    for label, record, expected in CASES:
        actual = predicate(record, 50)
        match = actual == expected
        print(f"{label:<20} {'Ready' if expected else 'Not ready':<12} "
              f"{'Ready' if actual else 'Not ready':<12} "
              + color_text("Yes" if match else "No", "success" if match else "failure"))


EQUIPMENT = [dict(record, id=f"E{index:02}")
             for index, (_, record, _) in enumerate(CASES, 1)]


def select_equipment(records, threshold=50):
    """Collect ready equipment and explain items needing attention."""
    if type(threshold) is not int or not 0 <= threshold <= 100:
        raise ValueError("Battery minimum must be an integer from 0 through 100.")
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
        excluded.append((record.copy(), reason))
    return selected, excluded


def show_report(records=EQUIPMENT):
    """Present a useful loan list without technical test output."""
    selected, excluded = select_equipment(records)
    print(color_text("Equipment Loan Desk - Classroom Loan List", "heading"))
    print("Request: Available equipment with at least 50% battery\n")
    print(color_text("Ready to borrow", "success"))
    for record in selected:
        print(color_text(f"  {record['id']} - Battery {record['battery']}%", "success"))
    if not selected:
        print(color_text("  No equipment meets this request.", "caution"))
    if excluded:
        print(color_text("\nNot included", "caution"))
        for record, reason in excluded:
            print(color_text(f"  {record.get('id') or 'Unidentified equipment'} - {reason}", "caution"))
    print(f"\nResult: {len(selected)} equipment item(s) ready to borrow.")


def continue_walkthrough(pause):
    """Pause for discussion and stop gracefully when console input ends."""
    if not pause:
        return True
    try:
        input("\nPress Enter for the next step...")
    except (EOFError, KeyboardInterrupt):
        print("\nWalkthrough stopped.")
        return False
    return True


def show_walkthrough(pause=True):
    """Connect purposeful tests, a boundary repair, and the useful loan list."""
    steps = [
        ("1. Problem and Precise Rule", "The desk needs available equipment with at least 50% battery.\nExactly 50% qualifies; unknown readings need checking. Predict 49%, 50%, and 51%."),
        ("2. Representation Bridge", "English: Trust the details, then require availability AND battery at least 50%.\nPseudocode: if valid AND available AND battery >= minimum: include equipment"),
        ("3. Deliberately Incorrect Rule", "Teaching only: battery > minimum. The normal report never uses this defect."),
        ("4. Repair and Regression", "Change > to >=. Only the boundary answer should change."),
        ("5. The Useful Answer", "Apply the corrected rule to the classroom loan inventory."),
    ]
    for index, (heading, explanation) in enumerate(steps):
        print(color_text("\n" + heading, "heading"))
        print(explanation)
        if index == 1:
            print(color_text("return valid_record(record) and record['available'] and record['battery'] >= threshold", "code"))
            print("Validation comes first so unknown readings are not compared with numbers.")
        elif index == 2:
            show_comparisons(buggy_predicate)
            print("The above-threshold happy path cannot reveal the boundary defect.")
        elif index == 3:
            show_comparisons(corrected_predicate)
            print("Unavailable and invalid items remain excluded. More checks are in test_demo.py.")
        elif index == 4:
            show_report()
        if index < 4 and not continue_walkthrough(pause):
            return


def main():
    """Separate the normal loan report from the guided teaching walkthrough."""
    while True:
        print(color_text("\nEquipment Loan Desk - Boundary Demo", "heading"))
        print("1. View the loan list\n2. Explore the teaching walkthrough\n0. Exit")
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
