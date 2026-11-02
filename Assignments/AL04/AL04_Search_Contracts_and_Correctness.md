# AL04: Search Contracts and Correctness

Week 4 | Individual work | Monday build, Tuesday checkpoint
Deadline: posted by your instructor; the checkpoint is formative, not a timed cutoff.

## Problem and Reading Connection

A campus help desk needs to locate tickets by ID or category. Implement a scan
and binary search that answer the same request under a shared result contract.
Explain when ordering makes binary search valid, including a deliberate failure.

Required weekly reading: Chapter 3 pp. 55-77, **Sorting and Searching Algorithms**.
This task applies linear/binary search, record keys, and preconditions. Other
chapter algorithms are not additional implementations. Start fresh: no AL03 code
or former partner's project is needed. Planned individual completion outside lab
is allowed; ask for help rather than abandon the Tuesday AL05 transition.

## Supplied Files and Setup

- `ticket_data.py`: six valid tickets in deliberately unsorted ID order.
- `search_support.py`: named `id_key`, `category_key`, `days_key`, `matches`, and
  `compare_values` helpers. These select/compare values; they do not traverse records.
- `ticket_display.py` and `console_style.py`: readable reports and small teaching traces.
- `README_Template.md`: short notes, not an extra evidence document.
- Optional `starter/main.py` and `starter/test_assignment.py`: unfinished English-first prompts.

Copy the two starter files beside the supplied modules if using them; do not run
them inside starter/. Keep one main.py, with assertions in test_assignment.py.
solution/ is the instructor's completed reference, not student starter material;
it is withheld until the grading period ends.

## Search Contracts

Implement in your `main.py`, with a short purpose docstring for each function:

| Function | Required Behavior |
| --- | --- |
| `linear_search(records, target, key=id_key)` | Scan in input order and return `(position, trace)` at the first match. Return `(None, trace)` when absent. Each trace entry is `(position, selected_value)`. |
| `binary_search(records, target, key=id_key)` | Search an inclusive low/high interval in input already ascending under key. Return `(position, trace)` or `(None, trace)`. Each entry is `(low, high, middle, selected_value)` before adjusting bounds. |

Both searches include the matching visit in the trace, return `(None, [])` for
empty input, and leave the list and records unchanged. Position 0 is valid;
`None` alone means absent. Resolve positions against the exact list searched.

The shared duplicate-key policy is **any match**. The linear scan returns first
because of its traversal; binary search may return another equal-key record.
Do not require first/last occurrence logic. IDs are unique, categories repeat.
Use `key=category_key` only with a category-ordered view for binary search.
Supplied fields/IDs are valid and values under a chosen key are comparable;
no schema validator, input menu, parser, or case-normalization feature is needed.

Ordering is the caller's responsibility. Do not scan to verify sortedness on every
binary query or secretly sort inside the search. Use `sorted(records, key=...)`
to prepare a view outside the algorithm. No timing or benchmark work.

## Build Across the Week

### Monday - Criteria, Scan, Then Binary Search

1. Create an individual AL04 folder, inspect the fresh records, and import the
   supplied helpers. Read `key(record)` as selecting a value, not performing search.
2. Implement linear search. Show found T403 and absent T499 with useful ticket
   details or a clear missing message; keep the original input order unchanged.
3. Implement binary search on an ID-ordered view. Use low=0, high=len(records)-1,
   integer midpoint, and bounds that move beyond the midpoint after a nonmatch.
4. Display the same found ticket from each path. Their positions can differ:
   T403 is input position 0 but ascending-ID position 2. Show one small linear
   trace and one small binary trace; label them as teaching views.
5. Demonstrate the supplied unsorted-order failure using T401: linear finds it,
   but binary search on the original list misses it. This is deliberate invalid
   use, not a correct alternative. Write one short reason why the discard failed.
6. Try the repeated category account under category_key, preparing a correctly
   ordered category view. Accept any returned matching category rather than
   demanding the same duplicate position from both searches.
7. Begin tests for found/missing, empty/singleton, endpoints, duplicates, and
   unchanged input. Commit the working baseline and brief README observations.

### Tuesday - Check, Correct, and Preserve the Submission

1. Use the checkpoint to show one result/trace and explain the ordering contract.
   Continue unresolved checks with instructor support; there is no automatic
   failure for not finishing at an exact point during class.
2. Finish independent expected outcomes, including first/last ID and absent
   targets below, between, and above present IDs. Check category duplicate behavior
   and the deliberate wrong-order example separately from valid-input tests.
3. Rerun app/tests. Record the any-match policy and precondition explanation in
   brief README notes, alongside your contribution, learning, and assistance.
4. Commit a complete AL04 snapshot in `week_04/AL04` in your own class repository.
   Submit that repository URL and folder path at the posted deadline.
5. For AL05, copy your completed traversal functions into its local
   `search_algorithms.py`; do not import a sibling main.py or keep editing the
   submitted AL04 snapshot. If unfinished, ask for the labeled recovery module.

## Check Your Work

Use independently expected records/results, not only agreement between two
possibly wrong implementations. Cover the behaviors above, not a fixed test
count. A deliberate invalid-order test is not a promise binary search will fail
on every unsorted input. The trace must include the actual visited values/bounds.
No separate trace report or mandatory pseudocode is required.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use python if it selects the course interpreter; do not use -O for tests.
Submit main.py, test_assignment.py, the four supplied support modules, and your
personal README.md. Keep imported files together and run the copied submission
from its final folder. Do not include starter/ or instructor solution files in
place of your completed work. Submit your own class-repository URL, not the
course-materials repository. No pair repository or formal peer-review post.

AI may explain, draft, debug, and support understanding checks under the standard
policy. Briefly identify assistance and what you checked/changed/rejected. Using
the starter or choosing not to use AI does not lower the grading ceiling.

## Evaluation Focus

Existing MRS descriptors apply; classifications do not introduce new weights.

### Primary

- T1 - Problem Framing and Algorithmic Analysis: key/result/precondition contracts.
- T3 - Algorithm Implementation and Testing: both traversals and focused cases.
- T4 - Correctness, Efficiency, and Tradeoff Evaluation: justified discards and qualified growth/setup reasoning.
- T5 - Observable Algorithm Behavior and Communication Evidence: two tiny traces and clear results.
- C1 - Solve Problems: connect valid lookup decisions to the help-desk request.

### Secondary

- T2 - Data Structures and Representation: record keys, duplicates, view-relative positions.
- T6 - AI/Data Foundations and Responsible Tool Use: evaluate/disclose assistance and supplied code.
- C2 - Communicate Clearly: concise contract and learning explanations.

### Light / Incidental

- C3 - Work Productively: staged progress and runnable submission.
- C4 - Value Learning: respond to evidence and feedback.
- C5 - Work Cooperatively: respectful questions/help within individual ownership; no partner or peer-review requirement.
- C6 - Act Professionally: accurate authorship and complete personal submission.

### Not Assessed

None designated. No required collaboration artifact or penalty for using no
outside assistance. Full duplicate-boundary algorithms remain optional depth.
