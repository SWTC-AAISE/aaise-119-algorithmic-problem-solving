# AL06: Nested Data — Recursion and Iteration

Week 5 | Individual work | Monday build, early Tuesday completion
Plan to finish and submit before AL07 paired work begins Tuesday. Your instructor will post the handoff/submission time.

## Problem and Reading Connection

Choose **one** application. Its groups may contain entries, other groups, or both.
Produce a useful total by including only the entries that meet its rule.

| Application / CHOICE | Include Only | Unit | Supplied Fixture's Expected Total |
| --- | --- | --- | ---: |
| Fundraiser Tracker / fundraiser | received donations | Whole dollars | 80 |
| Project Effort Estimator / project | unfinished tasks | Hours | 13 |
| Inventory Counter / inventory | usable stock | Items | 25 |

These choices have comparable structure and difficulty. You complete only your
chosen application. Storage Usage Analyzer is not an option. The records and
selection requirement differ from the folder demo: summing every amount will
give the wrong answer. Adapt the recursive/stack pattern to the status rule.

Read the assigned Chapter 4 selections and **all of Sweigart's Chapter 1,
[What Is Recursion?](https://inventwithpython.com/recursion/chapter1.html)**,
as listed in [Reading Assignments](../../Reading_Assignments.md).
Apply base cases, call/return, explicit pending work, and conditional selection.

## Supplied Files and Setup

- scenario_data.py: the three named fixtures, units, required statuses, and simple record builders.
- record_support.py: validate_node checks one record's shape and numeric policy.
- record_display.py and console_style.py: readable records, results, and optional color.
- README_Template.md: short personal work notes.
- Optional [Thinking Guide](AL06_Thinking_Guide.md): English-only reasoning for each choice. Read your chosen scenario if helpful; no written response is required.
- Optional starter/main.py and starter/test_assignment.py: one generic English-first
  scaffold for **any** choice, without the completed selection/traversal logic.

Create a fresh individual working folder. Copy the supplied modules and, if
using the starter, copy its two files beside them. Change CHOICE in main.py to
fundraiser, project, or inventory; no menu or argument parser is required.
The instructor's solution/ folder is withheld until the grading period ends.

## Record and Function Contracts

A group has type="group", name, and an items list. An entry has type="entry",
name, amount, and status. Group nesting is finite and acyclic. The supplied
records use nonnegative integer quantities; boolean, negative, fractional, or
missing amounts are invalid. Empty groups and zero amounts are valid.

Implement these top-level functions in main.py, each with a short purpose docstring:

| Function | Required Behavior |
| --- | --- |
| recursive_total(node, included_status) | Return an entry's amount only when its status equals included_status; otherwise return 0. For a group, recursively total its children. |
| iterative_total(node, included_status) | Use an explicit list stack to visit the same nested input and apply the same entry rule; return the selected total. |

Both return **one integer**, preserve the source, and call supplied validate_node
for every visited record. Invalid records raise ValueError even when their status
would exclude them. Treat the supplied included_status as the exact, case-sensitive
matching string; any valid entry with another status contributes zero.

The validation helper does not select entries or compute totals; those decisions
are your work in both traversals. A supplied display function is not your
iterative aggregation. Do not pre-flatten the data, hard-code the expected total,
silently skip malformed records, or substitute one implementation for both.
There is no nested-function/nonlocal requirement. Valid groups can be empty at any level.

## Build Across the Week

### Monday — Apply the Rule and Build Both Approaches

1. Choose one app and inspect its named fixture. Identify the included status,
   quantities, and units. Hand-check which entries contribute to the expected total.
2. Implement recursive_total. A qualifying entry returns its amount; an excluded
   entry returns zero. A group combines its children's returned subtotals; an
   empty group's result is zero. Include the supplied validation call.
3. Display the application/rule and useful result with units using the supplied
   helpers. Do not present a raw dictionary as the main user report.
4. Implement iterative_total using append/pop pending work on the **same input**.
   Both traversals must apply the status rule and preserve the data. They need
   not visit siblings in the same order to obtain the same sum.
5. Begin focused tests and commit a working baseline. Use the optional generic
   starter if useful; ask for help with one call/return or pending item rather
   than write a lengthy pre-code plan.

### Early Tuesday — Check, Submit, and Move to AL07

1. Check one useful result and one included/excluded entry. Bring any remaining
   difficulty to the instructor before the AL07 handoff.
2. Check empty groups, a single included/excluded entry, zero, a flat group,
   deeper/mixed nesting, all-excluded data, and unchanged source records.
3. Use a small fixture where equal amounts have different statuses; verify
   the rule, not only agreement between two potentially incorrect functions.
   Test malformed amounts/records through both functions, including an invalid
   excluded entry, under the supplied policy.
4. Add brief normal README observations about the approaches or a debugging
   discovery. No trace, diagram, presentation, or additional report is required.
5. Run the complete personal copy, commit/push, and submit before beginning AL07.
   If you are stuck, ask for help early so the assignments do not overlap.

Submit AL06 once. Successive commits show progress; separate daily code copies
are not required within AL06.

## Evidence and Workload

Keep evidence in the readable application, focused test_assignment.py, and brief
personal README. Briefly compare calls with an explicit stack, or describe a
learning/debugging observation. Do not claim one approach is always faster.

Plan for Monday's 70-minute lab and a short early-Tuesday finish: about 1–1.5
days, ending before AL07 starts. A few small fixtures can cover several checks;
a separate fixture for every listed case is unnecessary. This is first
recursion practice, not a timed competition. You do not need to build all three
apps, a UI framework, persistence, menus, a validation framework, or benchmarks.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use python if it selects the course interpreter; run assertions without -O.
Submit main.py, test_assignment.py, scenario_data.py, record_support.py,
record_display.py, console_style.py, and personal README.md together in
week_05/AL06 in **your own class repository**. Keep the chosen app independently
runnable; do not import a demo or sibling assignment. Submit that repository URL
and folder path in Schoology, not the course-materials repository. No pair repo
is needed for this individual assignment.

AI may explain, draft, debug, suggest checks, and support understanding under the
normal policy. Briefly identify assistance and what you checked/changed/rejected.
Using the optional starter or no AI does not reduce the grading ceiling.

## Evaluation Focus

Existing MRS descriptors apply; these classifications add no new weights.

### Primary

- T1 — Frame problems and analyze algorithmic requirements: chosen app, selected-entry rule, base cases, and result contract.
- T3 — Implement and test introductory algorithms using Python: recursive and stack traversals, rule adaptation, and focused checks.
- T4 — Evaluate correctness, efficiency, and tradeoffs among algorithmic approaches: independent expectations, preserved data, and qualified comparison.
- T5 — Use observable evidence to explain algorithm behavior: readable result and brief normal README observations.
- C1 — Solve Problems: produce the useful selected total for the chosen need.

### Secondary

- T2 — Select data structures and representations for algorithmic solutions: nested groups/entries and explicit pending state.
- T6 — Connect algorithmic thinking to AI, data systems, and responsible tool use: evaluate/disclose help and identify supplied material.
- C2 — Communicate Clearly: short rule and learning explanations.

### Light / Incidental

- C3 — Work Productively: staged progress and complete runnable submission.
- C4 — Value Learning: respond to debugging evidence and feedback.
- C5 — Work Cooperatively: respectful help/questions in normal course work; no formal review artifact.
- C6 — Act Professionally: individual ownership, accurate assistance notes, and submission completeness.

### Not Assessed

None designated. No separate collaboration artifact or outside assistance is
required to earn full credit.
