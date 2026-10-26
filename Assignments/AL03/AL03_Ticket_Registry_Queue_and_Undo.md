# AL03: Ticket Registry, Queue, and Undo

Week 3 | Paired programming | Individual submission
Deadline: provided by your instructor.

## Problem

A campus help desk needs to find support tickets, organize waiting work in arrival
order, and recover when someone accidentally marks a ticket completed. Cancelled
tickets must not remain in the waiting queue. A saved category report should
still show what was selected earlier, even when the live tickets change.

Build one small console application across Monday, Tuesday, and Thursday. Start
a fresh shared project with your new partner(s); neither partner's earlier code
is required. Submit once after the final stage. A scripted demonstration is
enough: no menu, database, file persistence, or ticket-entry interface is required.

## Reading Connection

Required: Chapter 2, pp. 25-53, Data Structures Used in Algorithmic Thinking.
Apply lists, dictionaries, sets, queues, and stacks to particular operations.
Recognize the other structures introduced in class without implementing them.
Optional Chapter 13 compression reading is not part of this assignment.

## Supplied Files and Setup

- `ticket_data.py`: six valid, fictional ticket records and supported categories.
- `ticket_display.py`: readable ticket reports and waiting-work/history summaries.
- `console_style.py`: the shared console-color helper used by the display module.
- `README_Template.md`: short personal notes and a three-row comparison.
- Optional `starter/main.py` and `starter/test_assignment.py`: English-first
  approach prompts, separated into Monday, Tuesday, and Thursday sections.

The `solution/` folder is the instructor's completed reference, not starter
material. Do not copy it into your assignment; release is after the grading period.

Keep these modules beside your own `main.py` and `test_assignment.py`. Adapt the
README template as `README.md`. The display helper contains no ticket operations;
you write the assessed functions and tests. If using the starter, copy its two
files into this same working folder, beside the supplied modules. Do not run
them from inside `starter/`; the imports expect the modules beside your code.
The starter supplies unfinished functions and test prompts, not a completed app.
No separate walkthrough is required. Explicit loops are welcome; compact syntax is optional.
Give each function a short purpose docstring. Keep assertions in the test file.

## Data and State Contracts

Each supplied ticket has `id`, `title`, `category`, `priority`, and `status`.
The records are flat: all field values are strings. Priorities are `low`, `normal`,
or `high`; statuses are `open` or `completed`. Use the supplied data unchanged.
Your examples may assume valid categories and priority values; a general input
validator is not required. Duplicate-ID rejection is required when building the registry.

The ID-keyed dictionary is the live registry. Its records must be independent
copies of the supplied records. Keep the original list only for lookup comparison,
not as a second live store that must track every change.

On Monday, use `SUPPORTED_CATEGORIES` for a set-membership check before selecting
a category. This vocabulary describes supported work, not just categories currently
represented in the registry. Do not remove categories when cancelling tickets.

On Tuesday, organize the application state using these names:

```python
from collections import deque

state = {
    "registry": registry,
    "pending": deque(),
    "undo": [],
}
```

`registry` here is the dictionary your Monday function built. Pending work stores
ticket IDs, not copied tickets. Undo history stores dictionaries with named fields
`ticket_id` and `previous_status`. The last history entry is the next action to undo.

### Functions You Write

| Day | Function in `main.py` | Required result / change |
| --- | --- | --- |
| Mon | `build_registry(records)` | Return an ID-keyed dictionary of independent flat record copies. Raise `ValueError` for a duplicate ID; never silently overwrite it. |
| Mon | `scan_lookup(records, ticket_id)` | Return the first matching record, or `None`. |
| Mon | `indexed_lookup(registry, ticket_id)` | Return the matching live record, or `None`, using dictionary lookup. |
| Mon | `update_priority(registry, ticket_id, priority)` | Change only that ticket's priority and return `True`. Return `False` without changes for a missing ID. |
| Mon | `filter_by_category(registry, category)` | Return a list of independent flat record copies matching the category, in registry iteration order. Return an empty list if none match. |
| Tue | `enqueue_ticket(state, ticket_id)` | Append a known, open ticket ID to pending and return `True`. Return `False` without any state changes for unknown, completed, or already-pending IDs. |
| Tue | `process_next(state)` | Remove the oldest pending ID, save its ID/prior status in undo history, mark it completed, and return its ID. Return `None` without changes for an empty queue. |
| Tue | `undo_process(state)` | Restore the latest successfully processed ticket's previous status, return its ID to the queue front, remove that history entry, and return the ID. Return `None` without changes for empty history. Preserve unrelated priority changes. |
| Thu | `repair_queue(registry, pending)` | Return `(repaired_queue, removed_ids)`: a new deque retaining known IDs in their original order, and a list of removed missing IDs in encounter order. Do not change either input. |
| Thu | `cancel_ticket(state, ticket_id)` | For an open ticket, remove its registry entry and any pending reference; return `True`. For a missing or completed ticket, return `False` with all state unchanged. Leave undo history unchanged. |

Ordinary pending work contains unique, known, open IDs. Processing and undo may
assume those rules hold. Test stale-ID repair separately using a deliberately
inconsistent queue, then install the returned queue before processing it.
The repair helper removes missing IDs only; it is not a general state-recovery engine.

Use `deque.append` / `popleft` for arrival-order processing, `appendleft` to
restore the undone request, and list `append` / `pop` for undo history. Undo
reverses processing only, not priority edits, cancellation, or every possible action.
No redo or priority-based scheduling is required.

## Build Across the Week

### Monday - Find, Update, and Select

1. Create the fresh shared AL03 project and import `TICKETS` and
   `SUPPORTED_CATEGORIES`. Inspect the six records together before building.
2. Implement `build_registry`, copying each flat record. Check that a separate
   duplicate-ID example is rejected rather than replacing an earlier ticket.
   Do not add a duplicate to the supplied `TICKETS` itself.
3. Implement list-scan and indexed lookup. Show the same found ticket through
   both approaches and a clear missing-ticket message. Compare before updates:
   the supplied list intentionally does not follow later registry changes.
4. Implement `update_priority`. For example, change T301 from normal to high.
   Show the updated ticket and check that the supplied record is unchanged.
   A missing ID must not create a ticket.
5. Use the supported-category set to check a category, then implement and show
   `filter_by_category`. For example, account selects T301 and T304 in the
   starting registry; classroom is supported but currently has no tickets.
   An unsupported category such as parking should receive a clear message.
6. Check found/missing lookup, empty input, duplicate IDs, priority updates,
   category selection, and independent copies. Save a filtered selection now
   so that you can revisit its independence on Thursday.
7. Begin the README's three-row lookup/update/filter comparison. Explain which
   representation fits each operation and why; do not build six parallel
   implementations or memorize an exhaustive cost table. Commit the baseline.

Stop here on Monday. Queues, processing, undo, and cancellation come after their
instruction. Use `display_tickets` to show lookup/category results; no state
summary is needed until Tuesday.

### Tuesday - Process in Order and Undo One Action

1. Continue the same project. Add the state dictionary, an empty pending deque,
   and an empty undo list. Keep the registry as the single live ticket store.
2. Implement `enqueue_ticket`. Queue T301 and then T302. Reject a repeated T301,
   unknown T999, and already-completed T306 without changing any state.
3. Implement `process_next`. Process those two requests, one at a time. The
   results must be T301 and then T302, regardless of their priority labels.
   Record only successful processing actions in undo history.
4. Implement `undo_process`. Undo once: T302 becomes open and returns to the
   front of pending; T301 remains completed. The T302 history entry is removed.
   Show enough information to make the processing/restoration understandable.
5. Check empty queue/history behavior, rejected requests, two processing actions,
   and successive undo behavior. Also change a processed ticket's priority before
   undoing it: undo must restore status without erasing that priority edit.
6. Add one brief README observation about the process/process/undo sequence.
   Run the earlier Monday checks again and commit progress. No trace essay or
   separate evidence document is required.

Your ticket-enqueue rule is stricter than the equipment demo: reject completed
tickets before they enter pending. Do not copy the demo's unavailable-item
request behavior into this application.

### Thursday - Cancel Consistently and Preserve Snapshots

1. Implement `repair_queue`. In a separate repair example, use pending IDs
   T301, T999, T302, T998 against a fresh registry. The returned queue must hold
   T301, T302; removed IDs must be T999, T998. The original queue is unchanged.
   Also check empty, all-valid, and all-missing queues.
2. In the application that owns the state, install the returned queue:

   ```python
   repaired, removed = repair_queue(state["registry"], state["pending"])
   state["pending"] = repaired
   ```

   Show the repaired waiting list and explain which unavailable requests were
   removed. Returning a repaired queue without using it does not fix live state.
3. Implement `cancel_ticket`. Cancel an open ticket that is pending, then an open
   ticket not pending. Other pending IDs retain their relative order. Reject
   missing/completed-ticket cancellation without changing registry, queue, or
   history. Completed-ticket cancellation is excluded so history stays valid.
4. Revisit a saved account selection from a fresh registry: save the selection,
   update T301's live priority, and cancel open T304. The earlier report still
   contains its original T301 values and its T304 record; the live registry does
   not. These are valid historical copies, not stale live queue references.
   Flat `record.copy()` is enough; no custom deep-copy algorithm is required.
5. Run all earlier tests, including processing/undo after the cancellation changes.
   Finish the three-row comparison and brief personal learning notes. Use ordinary
   independent fixtures so one demonstration does not accidentally change another.
6. Each partner copies the complete agreed application and supplied modules into
   their own class repository's `week_03` folder, adds a personal README, runs
   that copy, commits, pushes, and submits once.

## Display and Checks

The supplied helpers are presentation only:

```python
from ticket_display import display_state, display_tickets

display_tickets("Account requests", selected_records)
display_state("Waiting work after undo", state)
```

Both display functions return `None` and leave their inputs unchanged.
`display_tickets` takes a list of ticket records; for a found ticket you can pass
`[ticket]` after checking it is not `None`. Show a friendly missing result yourself.
`display_state` takes the Tuesday state dictionary. The helpers support plain
text when redirected and color in compatible terminals. You may adapt the display
without changing the required behavior. Avoid raw dictionary dumps as the main UI.

Keep assertions in `test_assignment.py`, using independently chosen expected
answers. Cover the behaviors in the daily stages, not a fixed assertion count.
For rejected actions, check **all** state components stay unchanged, not just
the return value. Verify that:

- Registry edits and filtered-record edits do not mutate the supplied records.
- Saved filtered records and live registry records do not mutate each other.
- Pending work stays unique, known, and open during normal operations.
- FIFO processing and LIFO undo restore the intended ticket and preserve other fields.
- Cancellation and repaired-queue installation leave no missing pending references.
- Repair preserves valid order without mutating its original queue.

No timing experiment, measurement framework, tree/graph implementation, external
package, parser, or new application interface is required.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use `python` if it selects the course interpreter. Run tests without `-O`.
Use a small scripted sequence in your `main.py` to show the daily behavior;
add each stage after its lecture. You do not need three separate applications.
The optional starter follows this same progression: fill in the relevant day's
functions and add calls to `main()` only when they work. Its initial main prints
a starting message; its unfinished tests deliberately fail rather than report
success without checks. Using the starter adds no writing requirement and does
not lower the grading ceiling.

Follow the [paired programming guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md):
work in Zoom breakout rooms, switch roles about every 20 minutes, and
commit/push/pull at handoffs. Partners rotate per assignment, not daily. Ask for
help in Zoom chat; arrange outside-lab Zoom sessions independently if needed.
There is no separate peer-review post for AL03.

Each student submits `main.py`, `test_assignment.py`, `ticket_data.py`,
`ticket_display.py`, `console_style.py`, a personal `README.md`, and any other
imported modules in their own class repository's `week_03` assignment folder.
Do not copy the shared repository's `.git` directory. Run the copied app and
tests before committing/pushing. In Schoology, submit **your own class repository
URL and folder path**, not the shared pair repository. One grade and one final
submission; your normal commits capture development across the week.

AI may explain, draft, debug, or support understanding checks. Record assistance
briefly, including what you checked, changed, or rejected; the standard course AI
policy applies. Choosing not to use AI or using available support does not lower
the grading ceiling. No mandatory pseudocode, pre-code essay, or extra reflection
form is required.

## Evaluation Focus

Existing MRS descriptors remain unchanged; these classifications add no weights.

### Primary

- T2 - Data Structures and Representation: independent records, supported-category
  set, registry, pending deque, and named-field undo history.
- T3 - Algorithm Implementation and Testing: correct operations and focused
  regression, rejection, empty-state, and independence checks.
- T4 - Correctness, Efficiency, and Tradeoff Evaluation: representation fit,
  FIFO/LIFO behavior, state consistency, and copy tradeoffs; no benchmarks.
- T5 - Observable Algorithm Behavior and Communication Evidence: readable results,
  visible processing/restoration, and concise operation comparisons.
- C1 - Solve Problems: connect operations to the help desk's workflow and recovery needs.
- C5 - Work Cooperatively: contribute, switch roles, and verify shared work.

### Secondary

- T1 - Problem Framing and Algorithmic Analysis: identify contracts and state rules.
- T6 - AI/Data Foundations and Responsible Tool Use: assess/disclose assistance and
  distinguish supplied data from student implementation.
- C2 - Communicate Clearly: brief explanations and personal learning notes.

### Light / Incidental

- C3 - Work Productively: staged progress and complete runnable files.
- C4 - Value Learning: respond to checks, mistakes, and feedback.
- C6 - Act Professionally: accurate contribution/assistance notes and personal submission.

### Not Assessed

None designated. Compact syntax, every taught set method, complete CRUD interfaces,
deep-copy internals, trees/graphs, and LRN features are not additional requirements.

## Optional Depth

Explain briefly why an earlier report may intentionally disagree with today's live
registry, or why a deque's constant-time end operations do not make duplicate
checking constant-time. Keep it qualitative; do not add a benchmark or undo framework.
