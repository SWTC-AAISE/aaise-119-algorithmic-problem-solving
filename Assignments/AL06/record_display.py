"""Supplied readable display; this module does not select or total amounts."""

from console_style import print_color
from record_support import validate_node


def show_records(node, unit):
    """Display names, quantities, and statuses while preserving visual input order."""
    pending = [(node, 0)]
    while pending:
        current, depth = pending.pop()
        validate_node(current)
        indent = "  " * depth
        if current["type"] == "entry":
            print(f"{indent}- {current['name']}: {current['amount']} {unit} [{current['status']}]")
        else:
            print(f"{indent}{current['name']}")
            for child in reversed(current["items"]):
                pending.append((child, depth + 1))


def show_results(scenario, recursive_result, iterative_result):
    """Present both results with the selected application, rule, and units."""
    print_color("\n" + scenario["title"], "heading")
    print("Include only entries marked: " + scenario["included_status"])
    print_color(f"Selected total: {recursive_result} {scenario['unit']}", "success")
    print(f"Explicit-stack total: {iterative_result} {scenario['unit']}")
