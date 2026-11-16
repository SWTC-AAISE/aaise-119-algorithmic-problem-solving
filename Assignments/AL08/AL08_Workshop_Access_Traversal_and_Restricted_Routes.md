# AL08: Workshop Access — Traversal and Restricted Routes

Week 6 | Monday individual model check; Tuesday/Thursday paired development;
Thursday individual restriction response | One final personal submission
Deadline: posted by your instructor.

## Problem and Reading Connection

A small workshop needs to show which rooms can be reached and provide a permitted
route from Entrance to Loading. A room may become unavailable, changing which
route can be used. Build a console planner using the supplied fictional network.

A node represents a room. An edge means a permitted direct passage, operating in
both directions. This model contains **12 rooms**, multiple routes, a cycle, and
a disconnected Annex. It omits physical distances, travel times, opening hours,
accessibility, and capacity. Fewest passages means **fewest hops**, not fastest travel.

Use Chapter 5's [assigned reading](../../Reading_Assignments.md): required
pp. 109–117 for graph meaning/representation/mechanics and pp. 125–132 for BFS/DFS.
Network analysis pp. 117–125 remains optional. Parent reconstruction and the
blocked-node contract are taught in Thursday's lecture/demo.

## Supplied Files and Setup

- network_data.py: common room graph, start/goal, and issued restriction options.
- network_support.py: model checks, clear defensive input errors, independent teaching snapshots, and Thursday-only parser wiring.
- network_display.py, app_runner.py, console_style.py: readable staged reports and colors.
- README_Template.md: short personal model, learning, contribution, and assistance notes.
- Optional starter/main.py and starter/test_assignment.py: one staged English-first scaffold for the whole week.

Keep the five runtime support files together: network_data.py, network_support.py,
network_display.py, app_runner.py, and console_style.py. Copy starter files beside
them if useful. Monday runs at STAGE=1 without calling unfinished traversals.
Raise STAGE to 2 for completed Tuesday work, then 3 for Thursday. The test starter
has its own TEST_STAGE switch, which must reach 3 before final submission.
The supplied validator is ready to use; you do not implement a second validator.
The instructor's solution/ stays withheld until grading ends.

## Ownership and Pair Operation

Monday's representation/checking work and brief notes are individual. Tuesday's
self-selected pairs/trio, with instructor support as needed, start from the same
fresh supplied files. No pair must choose whose earlier assignment or individual
Monday code becomes the app. Reuse your understanding and personal Monday notes.

Follow the [pairing/submission guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md):
work in Zoom breakout rooms, change driver/navigator about every twenty minutes,
commit/push before the next driver pulls, and include the third member in meaningful
checks/questions. Use chat to request help; arrange your own Zoom time if extra
joint work is needed. No assumption of an automatic pairing speedup.

Thursday, preserve the shared working baseline and copy it to each member's own
class-repository week_06/AL08 folder. Each member applies the issued case, adds
personal tests/notes, and runs that complete personal copy. Shared work is attributed;
the individual adaptation and explanations use each student's own understanding.

## Record and Function Contracts

The supplied graph is a finite undirected dictionary of ordered neighbor lists.
Keep the issued names and neighbor order. The validator checks duplicate, unknown,
and missing reciprocal references. A declared empty list is valid disconnected data.
Do not edit the main GRAPH to simulate a restriction; apply blocks per query.

Write these top-level functions in main.py, with a short purpose docstring each:

| Function | Required Behavior |
| --- | --- |
| breadth_first(graph, start) | Use a deque, mark discovered on enqueue, and return (order, trace, edges_examined). |
| depth_first(graph, start) | Use a list stack, mark visited when processing a popped entry, skip already-processed entries, and return (order, trace, edges_examined). |
| reconstruct_path(parents, goal) | Follow the existing parent chain backward to None; reverse the new result and return start-to-goal order. |
| shortest_hop_path(graph, start, goal, blocked=()) | Use BFS first-parent tracking and blocked-node membership; return (path, parents), or (None, parents) when no route remains. |

### Traversal Details

Visit only the component reachable from start and process each node once. BFS
considers listed neighbor order. DFS pushes reversed neighbors so the first listed
available neighbor is next. A duplicate pending DFS entry is skipped once processed;
there is no separate requirement to catalogue unusual traversal variants.

Increment edges_examined once per neighbor entry inspected for a newly processed
node. An undirected connection has two entries. Call supplied
record_step(trace, node, frontier, seen) after neighbor handling. For BFS, seen is
discovered; for DFS, it is visited. That helper supplies the copies/sorted labels;
you do not implement a trace framework. Returns match the Week 6 traversal demo.

Use supplied validate_request(graph, start) for clear errors. Both functions
preserve the graph. The trace describes state after each new visit; its membership
labels are alphabetical, not another traversal order.

### Route Details

Use validate_request(graph, start, goal, blocked_nodes) after converting incoming
blocked names to a set. Unknown requested/reference names raise supplied ValueError.
A blocked start or goal returns (None, {}). A valid unreachable goal returns None
with the parent state reached. An allowed start=goal returns [start] with zero hops.

Initialize parents with start:None. Save a neighbor's first parent before enqueueing
and use membership in parents to track discovery. Do not overwrite that first link.
Use reconstruct_path when the goal is reached. The helper receives a valid chain
produced by BFS; no separate arbitrary-parent validator is required.

Every returned route begins at start, ends at goal, follows permitted adjacent
connections, and excludes all blocked nodes. Return a **fewest-hop** route; neither
DFS's visit order nor BFS's complete visit list substitutes for the route.
Do not mutate graph, supplied block lists, or the parent map during reconstruction.

## Build Across the Week

### Monday — Interpret and Check the Model Individually

1. Copy the supplied modules and optional starter. Run STAGE=1 to inspect the room connections and supplied model check.
2. Read node/edge meaning and direction. Keep a brief representation in your README: the supplied readable adjacency output or a small diagram is sufficient; no second hand-drawn/code model is required.
3. Follow a cycle such as Reception–Hallway–Assembly–Inspection–Packing–Loading–Office–Reception. Explain why Annex is valid although unreachable from Entrance.
4. In your test file, make a separate copy of the neighbor lists. Introduce one unknown reference or missing reverse connection, check the reported issue, repair it, and check the model again. Preserve the source fixture.
5. Add a short model/omission and broken/repaired observation to the ordinary README. Commit progress; save these personal notes for the final copy.

Monday is representation practice, not early BFS/DFS implementation or a second
application. Supplied validation allows everyone to begin Tuesday from common files.

### Tuesday — Implement Traversals Together

1. Form the self-selected pair/trio and start the shared repository/application from fresh supplied data and scaffold files. Keep Monday's individual notes.
2. Implement breadth_first and depth_first separately. Use the supplied validation/snapshot helpers and ordinary loops/conditions.
3. Hand-check a tiny graph before using the full workshop. Compare reachable membership, the first few queue/stack changes, and the expected order under the listed neighbor policy.
4. On the workshop fixture, reach eleven rooms from Entrance; Annex is not reached. Both full traversals examine 26 adjacency entries representing thirteen two-way connections.
5. Test the selected order, a cycle without repeat processing, a disconnected start, source preservation, and a clear invalid-name result. A few small fixtures can cover several checks.
6. Set STAGE=2 and TEST_STAGE=2 when those implementations/checks are ready. Use the readable reports and supplied short state examples rather than writing another evidence report.
7. Rotate roles, commit/push progress, and note one useful pair question/decision plus your own contribution briefly. Leave path reconstruction and restrictions for Thursday's instruction.

Core traversal work is O(V+E); validation and snapshot/sorted-label overhead are
additional work. Explain the scope qualitatively. No timings or benchmark harness.

### Thursday — Add Routes, Then Make Your Personal Adaptation

1. Continue the pair's application. Add first-parent tracking and reconstruct_path to return a connected fewest-hop route.
2. Verify the baseline Entrance–Reception–Office–Loading: three hops. Check start=goal, disconnected Annex, a blocked endpoint, and unchanged source data using focused tests.
3. Verify one shared blocked-node query, then commit/push the shared baseline. Keep the supplied input/presentation helpers.
4. Copy the complete app into your own class repository's week_06/AL08 folder. Set MY_RESTRICTION to your instructor-issued A, B, or C case below; members use different cases where practical.
5. Add an independent expected result for your assigned case to your tests. Check endpoints/adjacent passages and excluded nodes for a returned path, or justify why no route remains. An unchanged route is valid evidence when the block does not affect it.
6. Set STAGE=3 and TEST_STAGE=3. Run the default app and all tests from your own complete folder. Briefly explain your result and assistance in your personal README.
7. Commit/push that personal copy and submit once using the posted deadline. Preserve the earlier assignments' complete folders.

### Issued Individual Cases

| Case | Blocked Nodes | Independently Checkable Expected Result |
| --- | --- | --- |
| A | Office | Entrance–Reception–Hallway–Assembly–Inspection–Packing–Loading; six hops. |
| B | Office and Packing | No route to Loading: both its neighboring access rooms are blocked. |
| C | Packing | Baseline three-hop route through Office remains available. |

The default app must show your saved issued case. Optional command-line overrides
are exploration; they do not replace that saved selection or its test/README finding.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Thursday's supplied interface also supports:

```powershell
py -3.14 main.py --blocked Office
py -3.14 main.py --blocked Office Packing
py -3.14 main.py --blocked
py -3.14 main.py --help
```

No --blocked option uses your saved personal case; --blocked alone supplies an
empty list. Parsing is introduced only in STAGE=3. Parser construction is supplied,
not assessed. Use python if it selects your course interpreter; test without -O.

Submit main.py, test_assignment.py, the five supplied runtime support modules,
and personal README.md together in **your own** week_06/AL08 folder. No imports
from a demo, another assignment, or a partner's machine. Schoology receives your
own class-repository URL and folder path, not the shared or materials repository.
The staged starter is optional support; all required algorithms/tests must be
complete and both stage settings final before submission.

## Evidence and Workload

Evidence stays in useful output, focused tests, a small purposeful state example,
and brief personal README notes covering representation, learning, cooperation,
and the individual restriction. No essay, mandatory pseudocode, separate evidence
report, formal peer-review session, graph library, weighted-path algorithm, blocked
edges, persistent storage, or extra UI. LRN is optional recognition, not a prerequisite.

Plan for Monday's 70-minute individual entry, Tuesday's 120-minute paired lab,
and Thursday's 120-minute shared-to-personal progression. These include questions,
role handoffs, checks and packaging; they are not all implementation minutes and
are not measured completion guarantees. Ask for help early rather than adding features.

Follow the default Manual First prompting practice to clarify the goal and expected
small behavior. AI may explain, draft, debug, suggest checks, or support understanding.
Justify actual help and what you checked, changed, or rejected in your README.
Using the optional starter or choosing not to use AI does not lower the grading
ceiling; a completed manual implementation is not a prerequisite for approved help.

## Evaluation Focus

Existing MRS descriptors apply; these classifications add no new weights.

### Primary

- T2 — Select data structures and representations for algorithmic solutions: room/connection meaning, adjacency order, queue/stack/set roles and parent links.
- T3 — Implement and test introductory algorithms using Python: BFS/DFS, reconstruction, permitted-route logic and focused checks.
- T5 — Use observable evidence to explain algorithm behavior: readable reached/route results, small snapshots, tests and concise personal observations.
- C1 — Solve Problems: connect representation, traversal and the changed access requirement.
- C5 — Work Cooperatively: role changes, useful questions/decisions, shared progress and complete personal handoff.

### Secondary

- T1 — Frame problems and analyze algorithmic requirements: goal, edge meaning, assumptions, blocks and result contracts.
- T4 — Evaluate correctness, efficiency, and tradeoffs among algorithmic approaches: independent expectations, fewest-hop claim, qualified work/storage reasoning and model limits.
- T6 — Connect algorithmic thinking to AI, data systems, and responsible tool use: evaluate/justify assistance and identify supplied/shared versus personal work.
- C2 — Communicate Clearly: brief model, traversal, contribution and restriction explanations.

### Light / Incidental

- C3 — Work Productively: staged progress, commits, handoffs and runnable personal files.
- C4 — Value Learning: apply reference material, feedback and test evidence.
- C6 — Act Professionally: accurate attribution, responsible tool use and complete submission.

### Not Assessed

None designated. Supplied validator, trace-copying, formatting and parser plumbing
are not independent implementation requirements. No additional collaboration or
support-use document is required.
