# AL05: Filter, Sort, and Search Pipeline

Week 4 | Individual work | Tuesday baseline, Thursday integration and revision
Deadline: posted by your instructor. Individual completion outside lab is permitted.

## Problem and Reading Connection

The help desk wants open tickets old enough for follow-up, displayed from fewer
to more days open, while still finding a chosen ticket by ID. Display order is
not necessarily a valid ID-search order. Build a clear pipeline using compatible
functions, then revise one eligibility requirement without rewriting algorithms.

Required weekly reading: Chapter 3 pp. 55-77, **Sorting and Searching Algorithms**.
Implement stable insertion sort and key-correct composition. Other sorts,
comparator adapters, timings, and a complete ticket-management app are not required.

## Files and Independent Setup

Supplied: fresh ticket_data.py, named-key/comparison helpers in search_support.py,
the tested filter in pipeline_support.py, ticket_display.py, console_style.py,
README_Template.md, and optional starter/main.py plus starter/test_assignment.py.
Copy the starter files beside these modules before running them.

Create a local `search_algorithms.py` containing copies of your AL04 traversal
functions and the imports they need. Do not import another assignment's main.py.
If AL04 is not ready, your instructor can release recovery/search_algorithms.py
after the AL04 checkpoint/release decision. Identify that module as supplied;
it is not your AL04 implementation and does not reduce AL05's grading ceiling.
Do not distribute recovery code to other students ahead of that release.

The recovery/ and solution/ folders are instructor-controlled release material,
not ordinary AL04 starters. Completed solutions are withheld through grading.
Each finished assignment must run independently in its own submission folder.

## Functions and Ownership

Implement in main.py with short purpose docstrings:

| Function | Required Contract |
| --- | --- |
| `insertion_sort(records, key)` | Return `(ordered, comparisons, moves, trace)`. ordered is a new shallow list, ascending under key. comparisons counts executed key comparisons in the shifting loop; moves counts right-shifts only, excluding final placements. trace contains the ID order after each insertion. Equal keys retain their relative input order. |
| `build_views(records, minimum_days=4)` | Return `(selected, display_view, search_view)`. Use the supplied open/age filter, your insertion sort under days_key for display, and ordinary `sorted(selected, key=id_key)` for the ID search view. |

Both functions leave the source list/order and record fields unchanged. Their
new lists intentionally share record dictionaries. This is not a Week 3 independent
snapshot: a new ordering is separate from a copied record. Do not silently add
record.copy() or deep-copy machinery to change this contract. Treat records as
read-only during each run and rebuild affected views after relevant changes.

The supplied filter includes all open tickets with days_open >= minimum_days.
Inputs are valid, flat records; minimum_days is a nonnegative integer. No input
validation framework, menu, parser, live edit interface, or persistence is required.
The search functions retain AL04's `(position, trace)` and any-match contracts;
only search an ID-ascending view for ID binary search.

## Build Across the Week

### Tuesday - Stable Ordering Baseline

1. Start your individual AL05 folder with the supplied modules and your local
   search_algorithms.py, or the instructor-released recovery copy. Keep AL04's
   submitted snapshot unchanged. Do not choose someone else's solution as a base.
2. Inspect the six tickets and the supplied filter. At minimum_days=4, selected
   IDs are T403, T405, T402, T406 in that order. T404 is completed and excluded.
3. Implement insertion_sort using a saved item, a sorted prefix, and right-shifts.
   Stop shifting on equality so T403 remains before T405, both age 7.
4. Show the age-ordered display: T406, T402, T403, T405. Capture one small trace
   and its counts: six key comparisons and five right-shifts for that selection.
   Label these as teaching evidence, not durations or universal costs.
5. Compare with sorted(records, key=days_key), then test empty/singleton, ordered,
   reverse, and shuffled inputs with ties. Verify input order/fields stay unchanged
   while returned lists share the record objects.
6. Commit the sort baseline. Briefly note one stability or copying observation;
   do not write a pre-code essay or another evidence file.

### Thursday - Compose, Change, and Verify

1. Implement build_views. Keep the age-ordered display separate from the ascending-ID
   search view. Display readable ticket details using the supplied helpers.
2. Find T403 through a linear scan of selected and binary search of search_view.
   Resolve each returned position in its own view; both identify the same ticket.
   Also show absent T499 and a clear empty-selection result at minimum_days=8.
3. Demonstrate the wrong-view risk using this fixture: ID binary search for T406
   on the age-ordered display misses a present ticket. Mark this as deliberate
   invalid use, not the correct workflow or an assertion every unsorted view fails.
4. Apply the issued change: raise minimum_days from 4 to 7. Rebuild from TICKETS;
   selected/display IDs become T403, T405, and T406 no longer qualifies. Do not
   rewrite the sort, search, equality, or key helpers. Rerun earlier checks.
5. Compare two workloads in brief README bullets: one request with only the source
   list ready, and repeated requests with a retained ID-ordered selection. Include
   filtering, sort setup, view storage, and rebuilding after the rule changes.
   No timings, measured winner, crossover claim, or multi-size experiment.
6. Finish the compact pipeline description, one changed/preserved observation,
   contribution/assistance notes, and tests. Run the complete independent copy in
   your own week_04/AL05 folder before committing/pushing and submitting.

## Evidence and Checks

Keep evidence lean: console result, one tiny insertion trace/count display,
focused tests in test_assignment.py, and the README's short pipeline/workload/
change/copy notes. A one-line flow such as source -> filter -> display/search
views -> lookup is enough; no diagramming tool, separate report, or duplicated
copy of every console trace is required.

Check boundary eligibility at days 4 and 7, completed-ticket exclusion, empty and
singleton inputs, sort stability, sorted parity, input nonmutation, shared-record
identity, found/missing lookup, view-relative positions, and rebuilding after change.
For stability, equal keys keep the order in the particular input supplied, even
if that input is reversed. No ID tie-break is added to the age sort.

Keep counts simple: small comparisons/right-shifts and optionally a selected
search trace. Do not instrument library sorting or add cmp_to_key/nonlocal counters,
timer/trial utilities, or retired AL02 measurement plumbing. Small counts do not
include every setup cost or prove equal-duration operations.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use python if it selects the course interpreter; do not use -O for tests. Submit
main.py, test_assignment.py, local search_algorithms.py, all five supplied Python
support modules, and your personal README.md. The optional starter is unfinished;
do not submit it in place of completed work. No runtime imports from AL04 or
other demos. Preserve the full AL04 copy separately for delayed grading/auditing.

Schoology: your own class-repository URL and week_04/AL05 folder path, not a shared
repo or course-materials URL. One final AL05 submission, with Tuesday/Thursday
progress in commits. No required pair activity or formal peer-review discussion.
AI can explain, draft, debug, or support understanding under the normal policy;
briefly disclose help and what you checked/changed/rejected. Using approved
recovery/starter support or no AI does not lower the grading ceiling.

## Evaluation Focus

Existing MRS descriptors apply; classifications do not introduce new weights.

### Primary

- T2 - Data Structures and Representation: distinct ordered views and explicit sharing.
- T3 - Algorithm Implementation and Testing: stable insertion sort and valid composition.
- T4 - Correctness, Efficiency, and Tradeoff Evaluation: stability, key preconditions, setup/reuse reasoning.
- T5 - Observable Algorithm Behavior and Communication Evidence: clear report, tiny trace, concise explanation.
- C1 - Solve Problems: connect follow-up eligibility, user display, and valid lookup.

### Secondary

- T1 - Problem Framing and Algorithmic Analysis: bounded pipeline and changed-rule contracts.
- T6 - AI/Data Foundations and Responsible Tool Use: evaluate/disclose AI and supplied recovery code.
- C2 - Communicate Clearly: short pipeline/workload/change notes.

### Light / Incidental

- C3 - Work Productively: staged commits and complete independent files.
- C4 - Value Learning: use regression evidence and feedback.
- C5 - Work Cooperatively: respectful questions/help without surrendering individual ownership; no partner or peer-review requirement.
- C6 - Act Professionally: accurate authorship/assistance and personal submission.

### Not Assessed

None designated. No collaboration artifact is required; absence of outside
assistance is not penalized. Full merge sort and first/last duplicate searches
remain optional later depth, not additional deliverables.
