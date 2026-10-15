"""Optional unfinished test scaffold; students choose expected lookup answers."""

from main import scan_lookup, build_index, indexed_lookup
from catalog_data import BOOKS, validate_book_ids


def assignment_checks():
    """Run focused checks based on AL02's lookup contracts."""
    # Monday: use the tiny library catalog and validate its IDs.
    # Predict first/last/missing answers before calling either lookup.
    # Check each implementation against those answers, not just against each other.
    # Example syntax only: assert 2 + 2 == 4
    # Tuesday: check empty input, repeated requests, order, and unchanged records.
    # Check rejection of duplicate IDs by the supplied precheck.
    # Thursday: rerun your checks after corrections and before copying/submitting.
    # Big-O labels and reasons belong in brief README notes, not timing assertions.
    # Replace this exception only after adding real executable assertions.
    raise NotImplementedError("Add your focused checks before reporting success.")


def main():
    """Reject unfinished or disabled tests before reporting success."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
