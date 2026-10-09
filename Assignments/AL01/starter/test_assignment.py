"""Optional test support; students supply their focused cases and expectations."""

from main import select_open_tickets, select_follow_up


def check_selection(selector, records, expected_ids, expected_issue_count):
    """Compare selected IDs and issue count with independently chosen expectations."""
    selected, issues = selector(records)
    assert [record["id"] for record in selected] == expected_ids
    assert len(issues) == expected_issue_count
    assert all(isinstance(issue, str) and issue.strip() for issue in issues)


def assignment_checks():
    """Run the focused checks you create from the assignment's coverage checklist."""
    # Example mechanics only: assert 2 + 2 == 4
    # Choose your records and predict outcomes from the policy, then call
    # check_selection or write direct assertions. Do not derive expected IDs
    # by calling the same selector you are testing.
    # Add checks as each day's policy is introduced; retain brief v1 notes.
    raise NotImplementedError("Add your assignment checks before reporting success.")


def main():
    """Run real checks without allowing unfinished or disabled tests to pass."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
