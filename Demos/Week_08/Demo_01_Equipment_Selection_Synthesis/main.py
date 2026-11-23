"""Check workshop laptop requests, then adapt to a longer session's battery rule."""

from equipment_data import EQUIPMENT, REQUESTS
from equipment_display import show_requests
from console_style import print_color


def eligible(row, minimum_battery):
    """Decide whether a device is an available laptop with enough battery."""
    if row["type"] != "laptop":
        return False
    if not row["available"]:
        return False
    return row["battery"] >= minimum_battery


def scan_requests(rows, queries, minimum_battery):
    """Check earlier-to-later records for each requested ID and return matches."""
    results = []
    for query in queries:
        found = None
        for row in rows:
            if row["id"] == query:
                if eligible(row, minimum_battery):
                    found = row
                break
        results.append(found)
    return results


def indexed_requests(rows, queries, minimum_battery):
    """Build an eligible-device index once, then answer this group of requests."""
    index = {}
    for row in rows:
        if eligible(row, minimum_battery):
            index[row["id"]] = row

    results = []
    for query in queries:
        results.append(index.get(query))
    return results


def main():
    """Show loan decisions, an equivalent approach and the changed battery policy."""
    print_color("WORKSHOP LAPTOP LOANS", "heading")
    print("Check which requested devices can be loaned for the workshop.")

    baseline = scan_requests(EQUIPMENT, REQUESTS, 50)
    show_requests("Initial workshop: available laptops, battery at least 50%",
                  EQUIPMENT, REQUESTS, baseline, 50)

    print_color("\nTeaching comparison: answer the SAME requests using an index", "heading")
    indexed = indexed_requests(EQUIPMENT, REQUESTS, 50)
    show_requests("Same workshop and policy", EQUIPMENT, REQUESTS, indexed, 50)
    print("The lookup approach changed; the loan requirements stayed the same.")

    revised = indexed_requests(EQUIPMENT, REQUESTS, 80)
    show_requests("Longer workshop: available laptops, battery at least 80%",
                  EQUIPMENT, REQUESTS, revised, 80)
    print("\nBirch laptop now needs charging. Cedar laptop is still ready to loan.")


if __name__ == "__main__":
    main()
