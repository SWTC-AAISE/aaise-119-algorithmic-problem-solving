# AL01 Full-English Walkthrough

Optional support, not an extra assignment. These steps explain an approach;
you do not need to submit answers or write pseudocode. Matching prompts appear
in `starter/main.py`.

## M - Monday: Find Open Tickets

First, look at one ticket's details. Decide whether its information can be used.
A missing or unacceptable value needs a checking message, not a guessed value.

For a valid ticket, check whether it is open. If it is, include it in the open
list. If it is closed, leave it out without calling it invalid.

Repeat for each ticket in its original order. Then show useful details, a count,
and a separate list of records needing checking. Say clearly if nothing matches.

Think about: **Is this ticket unusable, or simply not part of this list?**

## T - Tuesday: Find Tickets Requiring Follow-Up

Use the same validation approach. For each valid ticket, check open status and
whether it is at least two days old. Both conditions must hold.

Collect the matching tickets and display the initial policy with the results.
Try ages just below, exactly at, and just above the minimum. Investigate the
supplied defective comparison and repair it to match the wording.

Think about: **Does exactly two days satisfy "at least two"?**

## Th - Thursday: Narrow Follow-Up Without Breaking the Other Rules

Keep validity, open status, and minimum age mandatory. For a ticket meeting those
conditions, check the new alternatives: high priority or access category.
Either alternative is enough, but neither overrides the mandatory conditions.

Update the decision and report's policy label. Leave the open-ticket rule alone.
Check a deliberately changed answer and an answer that should stay the same.

Improve one small part of the code's organization, then rerun the same final-policy
tests. This refactor should preserve results.

Think about: **Did the requirement change, or did only the code organization change?**

## Connect the Approach to the Code

CORE is the relationship between trusting data, applying a rule, collecting
matches, and presenting an answer. BASE is the code and tests that make those
responsibilities work. SKY is the help desk's need for useful lists.

Start with one record, build, run, and improve. If a result surprises you, check
whether the rule was misunderstood or implemented incorrectly.

You may use bounded AI implementation help after explaining the intended behavior.
The starter's prompts are guidance, not a required architecture. Brief learning
notes belong in your normal README; using this support adds no writing requirement.
