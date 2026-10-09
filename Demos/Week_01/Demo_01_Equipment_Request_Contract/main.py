"""Demonstrate precise loan rules and present laptops ready to borrow."""

from console_style import color_text, print_color







EQUIPMENT = [
    {"id": "E01", "type": "laptop", "available": True, "battery": 80},
    {"id": "E02", "type": "laptop", "available": False, "battery": 95},
    {"id": "E03", "type": "tablet", "available": True, "battery": 70},
    {"id": "E04", "type": "laptop", "available": True, "battery": 50},
    {"id": "E05", "type": "laptop", "available": True, "battery": None},
]


def validate_record(record):
    """List equipment details that are missing or cannot be trusted."""
    errors = []
    for field in ("id", "type"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{field} must be nonempty text")
    if type(record.get("available")) is not bool:
        errors.append("available must be True or False")
    battery = record.get("battery")
    if type(battery) is not int or not 0 <= battery <= 100:
        errors.append("battery must be an integer from 0 through 100")
    return errors


def battery_meets_requirement(battery, minimum_battery):
    """Accept a validated battery reading at or above the minimum."""
    return battery >= minimum_battery


def exclusion_reason(record, requested_type, minimum_battery):
    """Explain why equipment is excluded, or return None when it qualifies."""
    errors = validate_record(record)
    if errors:
        if errors == ["battery must be an integer from 0 through 100"]:
            if record.get("battery") is None:
                return "Battery not recorded; check before lending"
            return "Battery reading needs checking; not selected"
        return "Equipment details need checking; not selected"
    if record["type"] != requested_type:
        return f"Not a {requested_type}; this request is for a {requested_type}"
    if not record["available"]:
        return "Already on loan"
    if not battery_meets_requirement(record["battery"], minimum_battery):
        return "Battery below the requested minimum; charge before lending"
    return None


def select_equipment(records, requested_type, minimum_battery=50):
    """Return selected copies and excluded copies with user-facing explanations."""
    if type(minimum_battery) is not int or not 0 <= minimum_battery <= 100:
        raise ValueError("minimum_battery must be an integer from 0 through 100")
    selected = []
    excluded = []
    for record in records:
        reason = exclusion_reason(record, requested_type, minimum_battery)
        if reason is None:
            selected.append(record.copy())
        else:
            excluded.append((record.copy(), reason))
    return selected, excluded


def render_report(selected, excluded, minimum_battery):
    """Build a readable laptop-loan report without exposing implementation details."""
    lines = [
        color_text("Equipment Loan Desk", "heading"),
        color_text("===================", "heading"),
        "Request: A laptop available to borrow today",
        f"Minimum battery: {minimum_battery}%",
        "",
        color_text("Ready to borrow", "success"),
    ]
    if selected:
        for record in selected:
            lines.append(
                color_text(
                    f"  {record['id']} - Laptop - Battery {record['battery']}%",
                    "success",
                )
            )
    else:
        lines.append(color_text("  No laptops meet this request.", "caution"))
    if excluded:
        lines.extend(["", color_text("Not included", "caution")])
        for record, reason in excluded:
            equipment_id = record.get("id") or "Unidentified equipment"
            lines.append(color_text(f"  {equipment_id} - {reason}", "caution"))
    count = len(selected)
    noun = "laptop meets" if count == 1 else "laptops meet"
    result_color = "success" if count else "caution"
    lines.extend(["", color_text(f"Result: {count} {noun} the request.", result_color)])
    return "\n".join(lines)


def show_report(minimum_battery=50):
    """Display the loan-desk answer using the corrected selection rules."""
    selected, excluded = select_equipment(EQUIPMENT, "laptop", minimum_battery)
    print(render_report(selected, excluded, minimum_battery))


def initial_battery_rule(battery, minimum_battery):
    """Illustrate the intentional boundary mistake; never use for actual loans."""
    return battery > minimum_battery


def walkthrough_cases():
    """Supply independently stated expectations for small, controlled examples."""
    return [
        (
            "Available laptop, battery 49%",
            {"id": "T01", "type": "laptop", "available": True, "battery": 49},
            False,
        ),
        (
            "Available laptop, battery 50%",
            {"id": "T02", "type": "laptop", "available": True, "battery": 50},
            True,
        ),
        (
            "Available laptop, battery 51%",
            {"id": "T03", "type": "laptop", "available": True, "battery": 51},
            True,
        ),
        (
            "Laptop on loan, battery 80%",
            {"id": "T04", "type": "laptop", "available": False, "battery": 80},
            False,
        ),
        (
            "Available tablet, battery 80%",
            {"id": "T05", "type": "tablet", "available": True, "battery": 80},
            False,
        ),
        (
            "Available laptop, unknown battery",
            {"id": "T06", "type": "laptop", "available": True, "battery": None},
            False,
        ),
    ]


def show_comparisons(cases, use_initial_rule=False):
    """Compare expected outcomes with the teaching mistake or actual selection."""
    print_color(f"{'Case':<34} {'Expected':<10} {'Actual':<10} Match?", "heading")
    print_color("-" * 65, "heading")
    for description, record, expected in cases:
        if use_initial_rule:
            # Initial examples isolate battery only: all are valid available laptops.
            actual = initial_battery_rule(record["battery"], 50)
        else:
            selected, _ = select_equipment([record], "laptop", 50)
            actual = bool(selected)
        expected_text = "Ready" if expected else "Not ready"
        actual_text = "Ready" if actual else "Not ready"
        match_text = "Yes" if actual == expected else "No"
        result_color = "success" if actual == expected else "failure"
        match_display = color_text(match_text, result_color)
        print(
            f"{description:<34} {expected_text:<10} {actual_text:<10} {match_display}"
        )


def continue_walkthrough(pause):
    """Pause for discussion, or stop gracefully when console input ends."""
    if not pause:
        return True
    try:
        input(color_text("\nPress Enter for the next step...", "heading"))
    except (EOFError, KeyboardInterrupt):
        print_color("\nWalkthrough stopped.", "caution")
        return False
    return True


def show_walkthrough(pause=True):
    """Connect an ambiguous request, precise rules, a correction, and a useful answer."""
    print_color("W01D01 - Precision and Correctness", "heading")
    print_color("\n1. Before Revision: An Ambiguous Request", "heading")
    print("Find an available laptop with enough battery for class.")
    print("What does available mean? How much battery is enough?")
    print("What should we do when the battery has not been recorded?")
    if not continue_walkthrough(pause):
        return

    print_color("\n2. After Revision: Precise Plain English", "heading")
    print("- Check that the equipment details are valid before trusting them.")
    print("- Select a laptop only when it is available to borrow.")
    print("- Its recorded battery must be at least 50%; exactly 50% qualifies.")
    print("- Exclude unknown or invalid details and explain what needs checking.")
    print("Input: inventory and a 50% minimum. Output: ready laptops and exclusions.")
    if not continue_walkthrough(pause):
        return

    print_color("\n3. Representation Bridge", "heading")
    print("Plain English: Battery at or above the minimum meets the requirement.")
    print_color("\nPseudocode", "heading")
    print("  for each equipment record:")
    print("      if details are invalid: explain what needs checking")
    print("      else if not a laptop: explain the different equipment type")
    print("      else if already on loan: explain it is unavailable")
    print("      else if battery is below the minimum: recommend charging")
    print("      else: include it in the ready-to-borrow list")
    print_color(
        "\nPython: the battery function used by the actual selection", "heading"
    )
    print_color("  def battery_meets_requirement(battery, minimum_battery):", "code")
    print_color(
        '      """Accept a validated battery reading at or above the minimum."""',
        "code",
    )
    print_color("      return battery >= minimum_battery", "code")
    print("The docstring explains purpose; the comparison implements the rule.")
    print_color("\nPython: collect the results after applying the rules", "heading")
    print_color("  for record in records:", "code")
    print_color(
        "      reason = exclusion_reason(record, requested_type, minimum_battery)",
        "code",
    )
    print_color("      if reason is None:", "code")
    print_color("          selected.append(record.copy())", "code")
    print_color("      else:", "code")
    print_color("          excluded.append((record.copy(), reason))", "code")
    print("\nNext: try battery > minimum. Predict the 49%, 50%, and 51% answers.")
    if not continue_walkthrough(pause):
        return

    cases = walkthrough_cases()
    print_color(
        "\n4. Initial Rule: Deliberately Incorrect (battery > minimum)", "caution"
    )
    print("These three records are valid available laptops; only battery varies.")
    print("Predict the result at exactly 50% before reading the comparison.")
    show_comparisons(cases[:3], use_initial_rule=True)
    print_color(
        "The 50% case fails: 'above' was coded instead of 'at least'.", "failure"
    )
    print("This teaching mistake is never used by the loan-desk report.")
    if not continue_walkthrough(pause):
        return

    print_color("\n5. Revised Rule: Correct (battery >= minimum)", "success")
    print("Change > to >=. These actual results use the application's selection.")
    show_comparisons(cases)
    print("Expected outcomes were stated first, independently of the algorithm.")
    print("The correction accepts 50% without admitting unavailable/unknown items.")
    if not continue_walkthrough(pause):
        return

    print_color("\n6. The Useful Answer", "heading")
    print("Now apply the corrected rules to the equipment desk's inventory.\n")
    show_report()


def main():
    """Let the user choose a normal report, guided walkthrough, or exit."""
    while True:
        print_color("\nEquipment Loan Desk - Demo Menu", "heading")
        print_color("1. View the loan-desk report", "success")
        print_color("2. Explore the teaching walkthrough", "heading")
        print("0. Exit")
        try:
            choice = input(color_text("Choose 1, 2, or 0: ", "heading")).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return
        if choice == "1":
            print()
            show_report()
        elif choice == "2":
            print()
            show_walkthrough()
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print_color("Please choose 1, 2, or 0.", "caution")


if __name__ == "__main__":
    main()
