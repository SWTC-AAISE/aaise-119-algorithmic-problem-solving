"""Optional English-first starter; develop one application across three days."""

from ticket_data import TICKETS


# ======================================================================
# MONDAY - Build the open-ticket view
# Begin after Monday's instruction. Work in this same file all week.
# ======================================================================

def validate_ticket(ticket):
    """Return readable issues, or an empty list when the ticket is valid."""
    # First, look at one ticket's information.
    # Check each required field against the assignment's accepted values.
    # A Boolean is not a recorded number of days.
    # If information cannot be trusted, collect a message saying what to check.
    # Identify the ticket, using a fallback if its ID is unusable.
    # Return your messages; no messages means the ticket is usable.
    raise NotImplementedError("Implement the ticket checks.")


def select_open_tickets(records):
    """Return (selected, issues) for the valid open-ticket view."""
    # Prepare a selected list and an issues list.
    # Look at each ticket in its original order.
    # Ask validation whether its information can be trusted.
    # If not, collect the issues and leave the ticket out.
    # Otherwise, include the ticket only if it is open.
    # A valid closed ticket is a nonmatch, not a data problem.
    # Return both lists without changing the original records.
    raise NotImplementedError("Build the open-ticket view.")


def show_report(title, policy, selected, issues):
    """Present useful ticket details, a count, and records needing checking."""
    # Identify the list and the policy used.
    # Show useful fields for each selected ticket, not its raw dictionary.
    # Say clearly when nothing matches, and show the selected count.
    # Show any checking messages in a separate section.
    # Optional: import color_text from the supplied console_style module.
    raise NotImplementedError("Build the readable report.")


def main():
    """Run the stages you have implemented so far."""
    # Monday: use TICKETS to select and display the open-ticket view.
    # Do not call unfinished Tuesday functions.
    # Replace this message as you build the application.
    print("AL01 starter: begin with the Monday section.")


# ======================================================================
# TUESDAY - Add the initial follow-up list
# Wait until Tuesday's instruction before beginning this stage.
# ======================================================================

def needs_follow_up(ticket):
    """Apply the current follow-up policy to a previously validated ticket."""
    # First, check whether the ticket is open.
    # Then check whether it is at least two days old.
    # Only a ticket meeting both conditions needs follow-up.
    # Exactly two days qualifies.
    # Return a yes/no decision.
    raise NotImplementedError("Implement the initial follow-up decision.")


def select_follow_up(records):
    """Return (selected, issues) for the current follow-up policy."""
    # Use the same validation and collection approach as the open view.
    # Collect messages for records whose information cannot be trusted.
    # For valid records, ask needs_follow_up whether they match.
    # Collect matches in their original order; return both lists.
    raise NotImplementedError("Build the follow-up list.")


# Add the follow-up selection and report to main once they work.
# Describe the initial policy in that report.
# Try ages below, exactly at, and above the minimum.
# Investigate and repair the assignment's supplied comparison defect.
# Keep brief observations in your README and commit your progress.


# ======================================================================
# THURSDAY - Revise the policy and refactor
# Wait until Thursday's instruction before beginning this stage.
# ======================================================================

# Edit the EXISTING needs_follow_up function; do not create another application.
# Keep valid data, open status, and the minimum age mandatory.
# For a ticket meeting those conditions, examine priority and category.
# Either high priority or the access category satisfies the new condition.
# Neither alternative can admit a closed or too-young ticket.
#
# Update the report's policy description. Leave the open-ticket rule unchanged.
# Check a result that should change and one that should remain the same.
# Improve one small part of the organization, then rerun the same final tests.
# A policy change may change answers; a refactor should preserve them.
#
# Continue using this main.py, commit your progress, and submit once.
# Append brief learning notes to your README; no separate walkthrough essay.


if __name__ == "__main__":
    main()
