# AL02: Library Catalog Lookup and Big-O Recognition

Week 2 | Paired programming | Individual submission
Deadline: provided by your instructor.

## Problem

A library needs to find books by catalog ID. Compare a list scan with an ID-keyed
dictionary, then recognize how the work changes as the catalog grows. A patron
may ask for one book; a circulation desk may handle many repeated ID requests.

This is one progressive assignment. Start Monday and add each stage after its
lecture and demo. Start a fresh shared project with your new partner(s).
Neither partner's AL01 code is the starting point. The supplied catalog is data,
not a working app; you implement the lookup algorithms yourselves.
Actual timing and performance experiments are parked for later.

## Reading Connection

Required: Chapter 1, pp. 12b-24, Performance Analysis through Summary.
Recognize input size, common growth classes, case-dependent work, and basic
time/space tradeoffs. Chapter 15, p. 438, is reference orientation only.
You are not being asked to reproduce every technique discussed in the reading.

## Supplied Files and Setup

- catalog_data.py: four book records (BOOKS) and a unique-ID precheck.
- growth_examples.py: four short examples to inspect and classify.
- README_Template.md: brief personal notes.
- Optional starter/main.py and starter/test_assignment.py: English-first
  approach prompts, not completed code or tests.

Keep the two supplied Python modules beside your own main.py and
test_assignment.py. You may copy the two optional starter files into that same
folder. Adapt the README template as README.md. Do not copy solution/, which
is the instructor's completed reference.

## Lookup Contracts

| Function in your main.py | Required result |
| --- | --- |
| scan_lookup(records, book_id) | First matching book, or None when absent. |
| build_index(records) | Dictionary mapping each unique catalog ID to its book record. |
| indexed_lookup(index, book_id) | Matching book, or None when absent. |

Each supplied record has id, title, and author fields. IDs are B1 through B4;
use the supplied records unchanged. This is catalog lookup, not title search,
loan processing, availability filtering, or a complete library-management system.

Use validate_book_ids(records) before comparing the approaches. Supplied
IDs are unique; the precheck rejects unusable/duplicate IDs rather than silently
resolving them. Leave input records unchanged. Both approaches must return
equivalent answers. Repeated requests retain their original order.

Use named functions with short purpose docstrings. Explicit loops meet the
requirements; compact syntax is optional. No counter function or measurement
infrastructure is required.

## Build Across the Week

### Monday - Implement and Recognize

1. Begin a fresh shared AL02 project. Import BOOKS and validate_book_ids from
   catalog_data.py; neither partner needs to copy a previous assignment.
2. Inspect the four supplied records: each has a catalog ID, title, and author.
   Validate the IDs before building an index.
3. Implement scan_lookup, build_index, and indexed_lookup. The scan stops at
   the first matching ID; the indexed lookup uses a dictionary already built.
4. Show a found book's ID, title, and author, and a clear message for an absent
   ID. Do not add a menu, borrowing system, or title-search feature.
5. Check both approaches against independently expected answers for B1, B4,
   an absent ID, and empty input. Keep the original catalog unchanged.
6. Briefly identify worst-case scan growth, index-build growth, and the expected
   average-case growth of one lookup in an existing index.
7. Commit the working baseline. Keep any useful challenge or learning observation
   in your normal README notes; no separate planning document is needed.

A single worst-case scan and index construction are O(n). One existing
dictionary-key lookup is expected average-case O(1). Include construction when
discussing a newly built index; do not call the whole process O(1).

### Tuesday - Recognize Growth Patterns and Cases

1. Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py.
   Use the catalog records for the first three; the halving example takes a size.
2. For each, record a Big-O label and one short reason in your README.
3. Explain why a request for B1 stops sooner than a request for B4 or an absent
   ID in this catalog order. Connect that observation to best/worst cases.
4. Finish focused tests for repeated requests, retained request order, unchanged
   records, and rejection of duplicate IDs by the supplied precheck.
5. Run the application and tests, correct mismatches, and commit progress.

The examples illustrate direct access, one pass, all ordered pairs, and repeated
halving. Recognize O(1), O(n), O(n^2), and O(log n); no formal proof is required.
You may run the four-book examples and halving_sizes(8) to see the pattern, but no
automated count table, timing report, or multi-size experiment is required.
The halving illustration is not a requirement to implement binary search.

A nested loop is not automatically quadratic: examine what each loop depends
on. Repeated scans are O(q*n); they become quadratic when q grows with n.
Typical or average-case behavior depends on the request assumptions, not just
the number of records. No average-case formula is required.

### Thursday - Choose Qualitatively and Submit

1. Recommend an approach for a patron's one B1 lookup when the catalog list is
   already available and no index has been built. Give a short reason.
2. Recommend an approach for a circulation desk's many repeated catalog-ID
   requests when it can retain an index. Give a short reason.
3. Explain the work to build that index, its additional storage, and why reusing
   it differs from rebuilding it for every request. No new feature is required.
4. Verify the final application and focused tests. Check that both lookup paths
   still return the same book details or the same absent result.
5. Each partner copies the complete agreed solution and supplied modules into
   their own class repository, adds personal README notes, and tests the copy.
6. Commit and push the personal copy, then submit your own repository URL and
   folder path. This is one final submission, not three separate daily apps.

Reason from the workload and code structure. You do not need measured evidence
or to prove one method is universally faster. No crossover discovery, memory
profiler, benchmark utility, or generated evidence.md belongs in this assignment.

## Check Your Work

Keep assertions in test_assignment.py. Cover these behaviors, not a fixed count:

- First and last match, absent ID, and empty input.
- Equivalent lookup answers, repeated requests, and preserved order.
- Unchanged input records.
- Duplicate-ID rejection by the supplied precheck.

Choose expected answers from the small fixture, not from the implementation
being tested. Do not assert exact timings or build a measurement framework.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use python if it selects the course interpreter. No packages, API, parser,
framework, extra application, or experiment runner is required. Run tests
without -O. Diagnostic output is appropriate for an algorithm lesson; show enough
book information to make a found/missing result understandable.

Use the optional starter's M/T/Th sections after the relevant instruction.
Keep one main.py throughout the week. Support adds no writing requirement and
does not lower the grading ceiling; no mandatory pseudocode or extra walkthrough.

Follow the [paired programming guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md):
Zoom breakout rooms, switches about every 20 minutes, and commit/push/pull
handoffs. Partners rotate per assignment, not per day. Use Zoom chat for help
and arrange your own outside-lab sessions if needed. No separate peer-review post.

Append brief personal README notes. The four labels/reasons, case observation,
and workload choices can be short bullets, not a book or separate worksheet.
Identify partners, contribution, assistance, and meaningful challenges/learnings.

Each member copies main.py, test_assignment.py, catalog_data.py,
growth_examples.py, personal README.md, and any imported support modules into
their own class-repository week_02 assignment folder. Do not copy the shared
.git directory. Run the copied files, commit/push, and submit your own class
repository URL plus folder path in Schoology. One final submission after Thursday.

AI may explain, draft, debug, or help recognize unfamiliar code. Supply relevant
code/context, assess the explanation, and briefly record assistance and what
you checked, changed, or rejected. AI may support understanding checks; your
explanation and reflections represent your own understanding and actual work.
The standard course AI policy applies.

## Evaluation Focus

Existing MRS descriptors remain unchanged; labels do not introduce new weights.

### Primary

- T3 - Algorithm Implementation and Testing: correct equivalent lookups and focused checks.
- T4 - Correctness, Efficiency, and Tradeoff Evaluation: recognition-level growth,
  case reasoning, and qualitative tradeoffs, not runtime experiments.
- T5 - Observable Algorithm Behavior and Communication Evidence: understandable
  results and brief code-based explanations, not a benchmark report.
- C1 - Solve Problems: connect lookup behavior to the request.
- C5 - Work Cooperatively: contribute, rotate roles, and verify joint work.

### Secondary

- T1 - Problem Framing and Algorithmic Analysis: identify input size and lookup contracts.
- T2 - Data Structures and Representation: use lists and ID dictionaries appropriately.
- T6 - AI/Data Foundations and Responsible Tool Use: evaluate and disclose assistance.
- C2 - Communicate Clearly: concise reasons and learning notes.

### Light / Incidental

- C3 - Work Productively: progressive commits and complete runnable files.
- C4 - Value Learning: respond to test observations and feedback.
- C6 - Act Professionally: honest contributions and complete personal submission.

### Not Assessed

None designated. Using optional support or choosing not to use AI does not lower
the grading ceiling. Technical rubric descriptors are applied at this week's
recognition depth; they do not authorize timing requirements.

## Optional Depth

Explain how retaining an index changes the amount of repeated construction, or
how changing hit positions affects a scan. Keep it qualitative. Optional depth
must not reintroduce the parked measurement work.
