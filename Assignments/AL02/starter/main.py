"""Optional English-first starter; one recognition-level app across three days."""

from catalog_data import BOOKS, validate_book_ids

# MONDAY - Implement equivalent lookups after Monday's instruction.


def scan_lookup(records, book_id):
    """Return the first matching book, or None when absent."""
    # Look at one record at a time, in its original order.
    # Compare its ID with the requested ID.
    # Return the record immediately when it matches.
    # Return None if you reach the end without a match.
    # Do not change the input records.
    raise NotImplementedError("Implement the first-match scan.")


def build_index(records):
    """Map each previously validated catalog ID to its book record."""
    # Begin with an empty dictionary.
    # Visit each book once; use its ID as the key and its record as the value.
    # Return the completed index without changing the original records.
    # Use the supplied ID precheck before building; do not resolve duplicates.
    raise NotImplementedError("Build the catalog ID index.")


def indexed_lookup(index, book_id):
    """Return the indexed book or None when the catalog ID is absent."""
    # Check whether the requested ID is a dictionary key.
    # Return the associated book when present; otherwise return None.
    # Do not rebuild the dictionary here.
    raise NotImplementedError("Query the existing index.")


def main():
    """Show the examples for the lookup functions you have completed."""
    # Begin a fresh shared project; do not choose either partner's AL01 code.
    # Use the supplied BOOKS list and validate its catalog IDs.
    # Build an index once; try first, last, and missing IDs.
    # Compare both lookup answers and show ID, title, author, or a not-found message.
    # Replace this message when the Monday functions are ready.
    print("AL02 starter: begin with the Monday section.")


# TUESDAY - Recognize growth; wait for Tuesday's instruction.
# Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py.
# Ask whether each examines one item, visits every item, visits every pair,
# or repeatedly reduces the remaining size.
# Give each a Big-O label and one brief reason in your README.
# Explain how a first-match scan differs from a last-match or absent-ID scan.
# Finish focused tests for empty input, repeated queries, order, and unchanged data.
# No counter function, timer, benchmark runner, or experiment report is needed.

# THURSDAY - Choose qualitatively and submit after Thursday's instruction.
# Consider a patron's one first-book request when the catalog list is available.
# Contrast it with a circulation desk's repeated IDs when an index can be reused.
# Explain construction and extra storage, not a measured speed winner.
# Add brief choices, learning, contribution, and assistance notes to the README.
# Copy the full app, data, growth examples, tests, and imported support modules
# into your own class repository; test the copy and submit your own URL.
# Keep this same main.py all week; no artificial extra feature or report.


if __name__ == "__main__":
    main()
