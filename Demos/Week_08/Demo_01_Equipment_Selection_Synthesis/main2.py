"""Annotated equivalent of main.py: connect the code to synthesis concepts.

Read the short version first. These comments explain the same algorithm and output.
"""

from equipment_data import EQUIPMENT, REQUESTS
from equipment_display import show_requests
from console_style import print_color


# ONE POLICY, TWO LOOKUP APPROACHES
# Keep the business decision in one function so changing lookup strategy does not
# accidentally change what qualifies. The record fields are valid in this fixture.
def eligible(row, minimum_battery):
    """Decide whether a device is an available laptop with enough battery."""
    # Reject a tablet even when it is available and well charged.
    if row["type"] != "laptop":
        return False
    # A checked-out laptop cannot satisfy a new loan request.
    if not row["available"]:
        return False
    # "At least" includes the boundary itself: 50 qualifies at 50, and 80 at 80.
    # The threshold is an argument, so the later rule change needs no new algorithm.
    return row["battery"] >= minimum_battery


# APPROACH 1: LOOK THROUGH THE INVENTORY FOR EACH REQUEST
# Keep one result per query, including None for an unknown or ineligible device.
# Preserving request order matters when matching results back to people.
def scan_requests(rows, queries, minimum_battery):
    """Check earlier-to-later records for each requested ID and return matches."""
    results = []
    for query in queries:
        # Reset for EACH query so a previous success cannot leak into a later result.
        found = None
        for row in rows:
            # Finding the requested ID and meeting the loan policy are separate checks.
            if row["id"] == query:
                if eligible(row, minimum_battery):
                    found = row
                # IDs are unique. Once this ID is found, another record cannot
                # satisfy the same request, even if this device is ineligible.
                break
        # Append None too: do not drop unsuccessful requests or reorder the list.
        results.append(found)
    return results


# APPROACH 2: PREPARE ELIGIBLE DEVICES ONCE FOR THIS GROUP OF REQUESTS
# This dictionary is FILTERED by the current policy. Building it visits the inventory;
# do not call that setup free or claim every small request becomes faster.
def indexed_requests(rows, queries, minimum_battery):
    """Build an eligible-device index once, then answer this group of requests."""
    # This is local state, rebuilt on each function call for the supplied threshold.
    index = {}
    for row in rows:
        if eligible(row, minimum_battery):
            # Use the ID as the key and retain the original record as the value.
            # Neither approach edits these records; this is not an independent deep copy.
            index[row["id"]] = row

    results = []
    for query in queries:
        # get returns the eligible record or None without a new inventory scan.
        # Extra dictionary storage buys reusable membership access within this call.
        results.append(index.get(query))
    return results


# DELIVERY SEQUENCE
# First solve the loan problem. Compare approaches with the SAME 50% policy.
# Only then change the battery rule to 80%, keeping the indexed approach fixed.
# This isolates the effect of a policy change from the choice of lookup method.
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

    # The eligible-only index must reflect the new rule. Calling again builds it
    # afresh, excluding Birch at 50% while retaining Cedar at exactly 80%.
    # An ID index holding ALL records need not be rebuilt merely because a separate
    # eligibility argument changes. The need depends on what the index stores.
    revised = indexed_requests(EQUIPMENT, REQUESTS, 80)
    show_requests("Longer workshop: available laptops, battery at least 80%",
                  EQUIPMENT, REQUESTS, revised, 80)
    print("\nBirch laptop now needs charging. Cedar laptop is still ready to loan.")


if __name__ == "__main__":
    main()
