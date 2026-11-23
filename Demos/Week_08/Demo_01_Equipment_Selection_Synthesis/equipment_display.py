"""Present useful loan decisions while keeping formatting out of the algorithms."""

from console_style import print_color


def show_requests(title, rows, queries, results, minimum_battery):
    """Explain each requested device's result using the original catalog details."""
    print_color("\n" + title, "heading")
    if not queries:
        print("No equipment requests to check.")
        return

    catalog = {}
    for row in rows:
        catalog[row["id"]] = row

    for position in range(len(queries)):
        query = queries[position]
        result = results[position]
        known = catalog.get(query)
        if result is not None:
            print_color(f"  {query} - {result['name']}: READY TO LOAN ({result['battery']}%).",
                        "success")
        elif known is None:
            print_color(f"  {query}: No equipment found with this ID.", "caution")
        elif known["type"] != "laptop":
            print(f"  {query} - {known['name']}: This request needs a laptop.")
        elif not known["available"]:
            print(f"  {query} - {known['name']}: Already checked out.")
        elif known["battery"] < minimum_battery:
            print(f"  {query} - {known['name']}: Battery {known['battery']}%; needs at least {minimum_battery}%.")
        else:
            print_color(f"  {query} - {known['name']}: No qualifying result was returned; review this request.",
                        "caution")
