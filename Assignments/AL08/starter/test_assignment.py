"""Optional focused check starting points; expand them across the week."""

from network_support import validate_model
from main import breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION

TEST_STAGE = 1  # Raise to 2 Tuesday and 3 Thursday after completing those tests.


def test_model():
    """Begin Monday with a clearly valid two-way model and an unknown reference."""
    assert validate_model({"A": ["B"], "B": ["A"]}) == []
    assert validate_model({"A": ["Missing"]})
    # Add your one broken-and-repaired copy of the workshop model.


def test_traversals():
    """Check independent expectations before trying the full workshop fixture."""
    tiny = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": []}
    # Assert expected orders, no repeated processing, four adjacency entries,
    # and source preservation using both functions.
    raise NotImplementedError("Add Tuesday's focused traversal checks.")


def test_paths_and_personal_case():
    """Check route boundaries and your issued blocked-node result independently."""
    # Check a small known path, start=goal, disconnected goal, and a blocked endpoint.
    # Import the supplied workshop data and use MY_RESTRICTION for your personal case.
    # Check exact expected endpoints/hops or None, consecutive connections, no blocked
    # rooms in a returned route, and unchanged source data.
    raise NotImplementedError("Add Thursday's path and personal-case checks.")


if __name__ == "__main__":
    test_model()
    if TEST_STAGE >= 2:
        test_traversals()
    if TEST_STAGE >= 3:
        test_paths_and_personal_case()
    print("Selected-stage starting checks passed; complete all stages before submission.")
