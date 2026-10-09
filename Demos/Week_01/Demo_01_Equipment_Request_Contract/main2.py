"""Equipment loan request demo with teaching-oriented comments.

This version of the application preserves the original classroom demo while
adding explanatory documentation. The main goal is to show how a vague request
for equipment becomes a precise rule set, how those rules are translated into
code, and how the final program produces a useful loan-desk answer.

The script supports two related outcomes:
1. Generate a practical equipment-loan report for laptops.
2. Walk through the reasoning that leads from ambiguous language to correct
   boundary-aware logic.
"""

from console_style import color_text, print_color


# Centralize ANSI styles so the rest of the code can refer to simple names.






# Sample inventory used by the loan-desk report and walkthrough.
EQUIPMENT = [
    {"id": "E01", "type": "laptop", "available": True, "battery": 80},
    {"id": "E02", "type": "laptop", "available": False, "battery": 95},
    {"id": "E03", "type": "tablet", "available": True, "battery": 70},
    {"id": "E04", "type": "laptop", "available": True, "battery": 50},
    {"id": "E05", "type": "laptop", "available": True, "battery": None},
]


def validate_record(record):
    """Collect validation issues for one equipment record.

    Args:
        record: A dictionary describing one equipment item.

    Returns:
        list[str]: A list of user-facing validation messages. An empty list means
        the record can be trusted for later selection checks.
    """
    errors = []

    # These text fields must exist before the record can be shown meaningfully.
    for field in ("id", "type"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{field} must be nonempty text")

    # Availability must be an actual Boolean so the rule stays unambiguous.
    if type(record.get("available")) is not bool:
        errors.append("available must be True or False")

    # Battery must be a valid percentage before we compare it to a threshold.
    battery = record.get("battery")
    if type(battery) is not int or not 0 <= battery <= 100:
        errors.append("battery must be an integer from 0 through 100")

    return errors


def battery_meets_requirement(battery, minimum_battery):
    """Apply the corrected battery rule used by the application.

    Args:
        battery: A validated battery percentage.
        minimum_battery: The minimum required battery percentage.

    Returns:
        bool: True when the battery is at or above the requested minimum.
    """
    # The phrase "at least" maps directly to >= in the corrected rule.
    return battery >= minimum_battery


def exclusion_reason(record, requested_type, minimum_battery):
    """Explain why a record is excluded from the ready list.

    Args:
        record: A dictionary describing one equipment item.
        requested_type: The type of equipment requested by the user.
        minimum_battery: The minimum required battery percentage.

    Returns:
        str | None: A user-facing exclusion reason, or `None` when the record
        qualifies for selection.
    """
    # Validate first so later checks do not rely on missing or untrusted data.
    errors = validate_record(record)
    if errors:
        # Battery-only issues get a more specific message for the desk staff.
        if errors == ["battery must be an integer from 0 through 100"]:
            if record.get("battery") is None:
                return "Battery not recorded; check before lending"
            return "Battery reading needs checking; not selected"
        return "Equipment details need checking; not selected"

    # Once data is trusted, check the request rules in user-facing order.
    if record["type"] != requested_type:
        return f"Not a {requested_type}; this request is for a {requested_type}"
    if not record["available"]:
        return "Already on loan"
    if not battery_meets_requirement(record["battery"], minimum_battery):
        return "Battery below the requested minimum; charge before lending"
    return None


def select_equipment(records, requested_type, minimum_battery=50):
    """Split equipment into selected and excluded groups.

    Args:
        records: A sequence of equipment dictionaries to evaluate.
        requested_type: The type of equipment requested by the user.
        minimum_battery: The minimum required battery percentage.

    Returns:
        tuple[list[dict], list[tuple[dict, str]]]: Copies of qualifying records,
        plus copies of excluded records paired with a reason.

    Raises:
        ValueError: If `minimum_battery` is not an integer from 0 through 100.
    """
    # Reject invalid thresholds before attempting any record-level decisions.
    if type(minimum_battery) is not int or not 0 <= minimum_battery <= 100:
        raise ValueError("minimum_battery must be an integer from 0 through 100")

    selected = []
    excluded = []
    for record in records:
        reason = exclusion_reason(record, requested_type, minimum_battery)
        if reason is None:
            # Copy qualifying records so later mutation does not affect the report.
            selected.append(record.copy())
        else:
            excluded.append((record.copy(), reason))
    return selected, excluded


def render_report(selected, excluded, minimum_battery):
    """Build the final text report for the loan desk.

    Args:
        selected: Records that satisfied the request.
        excluded: Records excluded from the request, paired with reasons.
        minimum_battery: The minimum battery percentage shown in the report.

    Returns:
        str: A formatted multi-line report ready to print.
    """
    # Assemble the report as text lines so presentation stays easy to adjust.
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

    # Explanations for exclusions help students see rule outcomes, not just results.
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
    """Print the user-facing loan-desk answer.

    Args:
        minimum_battery: The minimum required battery percentage.

    Returns:
        None: This function prints the rendered report.
    """
    # Reuse the same selection path as the rest of the application.
    selected, excluded = select_equipment(EQUIPMENT, "laptop", minimum_battery)
    print(render_report(selected, excluded, minimum_battery))


def initial_battery_rule(battery, minimum_battery):
    """Demonstrate the intentional boundary mistake for the walkthrough.

    Args:
        battery: A validated battery percentage.
        minimum_battery: The minimum required battery percentage.

    Returns:
        bool: True only when the battery is strictly above the minimum.
    """
    # This is the teaching bug: exact-boundary values are incorrectly rejected.
    return battery > minimum_battery


def walkthrough_cases():
    """Return controlled examples for the guided walkthrough.

    Returns:
        list[tuple[str, dict, bool]]: Descriptions, input records, and expected
        outcomes stated independently of the implementation.
    """
    # These cases isolate both the battery boundary and other exclusion reasons.
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
    """Print expected and actual results for walkthrough examples.

    Args:
        cases: The walkthrough cases to compare.
        use_initial_rule: True to use the intentionally buggy boundary rule,
        False to use the application's real selection logic.

    Returns:
        None: This function prints a comparison table.
    """
    print_color(f"{'Case':<34} {'Expected':<10} {'Actual':<10} Match?", "heading")
    print_color("-" * 65, "heading")
    for description, record, expected in cases:
        if use_initial_rule:
            # The first battery-only examples assume valid available laptops.
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
    """Pause between walkthrough sections when requested.

    Args:
        pause: True to wait for user input between sections, False to continue
        without stopping.

    Returns:
        bool: True when the walkthrough should continue, otherwise False.
    """
    if not pause:
        return True

    try:
        input(color_text("\nPress Enter for the next step...", "heading"))
    except (EOFError, KeyboardInterrupt):
        # Treat interrupted input as a graceful exit from the lesson.
        print_color("\nWalkthrough stopped.", "caution")
        return False
    return True


def show_walkthrough(pause=True):
    """Lead the user from ambiguous wording to corrected program logic.

    Args:
        pause: True to pause between sections, False to run straight through.

    Returns:
        None: This function prints the teaching walkthrough.
    """
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

    # Show the exact function that turns the plain-English rule into code.
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
    """Run the menu for the report, the walkthrough, or exit.

    Returns:
        None: This function manages the demo menu until the user exits.
    """
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

        # Keep each menu choice mapped to one clear user-facing action.
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
