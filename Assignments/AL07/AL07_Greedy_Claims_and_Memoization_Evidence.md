# AL07: Greedy Claims and Memoization Evidence

Week 5 | Paired work | Tuesday build, Thursday enhancement | One final submission
Deadline: posted by your instructor.

## Problem and Reading Connection

A largest-first payment rule is easy to follow. Does it always produce an exact
payment using the fewest coins? Build a small payment planner and use a supplied
reference to test that claim. Then investigate a different question: can saving
previously calculated answers reduce repeated work without changing a result?

These are **two small investigations**, not two competing solutions to one problem.
The Fibonacci calculation does not improve or replace the payment planner.

Use Week 5's required readings in [Reading Assignments](../../Reading_Assignments.md):
greedy strategy pp. 92–93, dynamic programming pp. 90b–91, and Sweigart's entire
Chapter 1 for recursion/call-stack foundations. The recurrence, memoization, and
counter conventions are taught in Thursday's lecture/demo; the textbook does not
supply this specific implementation.

## Working Together and Setup

Finish/submit individual AL06 before starting AL07. Begin with your newly assigned
pair/trio and fresh supplied files; neither partner's AL06 code is needed.

Use the [pairing/submission guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md).
Work in a shared repo in your Zoom breakout room, switching driver/navigator about
every 20 minutes. Commit and push before the next driver pulls. Include the third
member meaningfully in questions/checks when working as a trio. Ask for instructor
help through chat; arrange any additional joint Zoom time yourselves.

Copy these supplied files into your working folder:

- coin_cases.py: four bounded payment cases.
- reference_solver.py: exhaustive minimum-coin reference; do not reimplement it.
- investigation_support.py: validation, reference wrapper, uncached recurrence,
  and fresh-cache/counter wrappers.
- investigation_display.py and console_style.py: readable reports, colors, and
  supplied Thursday command-line wiring.
- README_Template.md: copy as your personal README.md for submission.

The optional starter/main.py and starter/test_assignment.py go beside these
modules. They provide the recurrence and English-first prompts, not the completed
assessed greedy/cache logic. Starting without them does not change requirements
or the grading ceiling. The instructor solution/ is withheld until grading ends.

## Contracts

### A. Exact Payments

Implement greedy_change(denominations, target) in main.py with a purpose docstring.
Call supplied validate_change, which returns distinct values in largest-first
order without changing the original list. Choose the largest fitting coin until
it no longer fits, then consider the next value. Unlimited coins are available.

- Objective: an **exact** payment using as few coins as possible.
- Denominations: nonempty list of positive integers; duplicates and unsorted input
  are accepted and normalized by supplied validation. Boolean values are invalid.
- Target: integer 0–12 inclusive; invalid inputs raise ValueError.
- Return a list of selected coins for an exact greedy payment. Zero returns [].
- Return None when the greedy process leaves an unpaid remainder. This alone
  does **not** prove the amount is impossible.
- Do not mutate the supplied list or replace the greedy implementation with the
  exhaustive solver. Use exhaustive_change separately as the reference.

| Supplied Case | What to Establish |
| --- | --- |
| Coins 1, 4, 6; amount 8 | Greedy pays exactly but uses more coins than necessary. |
| Coins 4, 6; amount 8 | Greedy gets stuck although an exact payment exists. |
| Coins 4, 6; amount 7 | The reference also finds no exact payment. |
| Coins 1, 5, 10; amount 12 | Both methods reach the same minimum count for this case. |

Compare exactness and coin counts, not a particular ordering of the reference's
coins. Agreement on one example does not prove a universal optimality claim.

### B. Saved Answers

Complete calculate_cached(n, cache, counts) in main.py. The supplied scaffold
already contains the recurrence F(0)=0, F(1)=1, and F(n)=F(n−1)+F(n−2).
Add explicit dictionary lookup and storage; keep top-level helpers and a short
docstring. No nested function, nonlocal, decorator, generator, or new DP design.

- Count every helper invocation, including calls that find a saved answer.
- Use membership to recognize a saved input; a saved answer of zero is valid.
- On a hit, increment counts["hits"] and return the saved answer.
- Otherwise calculate the answer, store it under n (including base cases), and return it.
- Use the supplied cached_fibonacci wrapper: it validates integer n in 0–20 and
  creates an empty cache and fresh counters for **each** comparison.
- Use supplied uncached_fibonacci for the before comparison. Do not rewrite it.

Wrappers return numeric answers and counts; the cached wrapper also returns its
cache for inspection. The internal recursive helper receives validated inputs
and shared per-run state; it is not a separate user-input validation task.

## Build Across the Week

### Tuesday — Challenge the Greedy Claim

1. Close AL06, form the assigned pair/trio, and copy fresh AL07 support files into
   the shared working folder. Keep ENABLE_MEMOIZATION = False for this stage.
2. Identify what “best” means and inspect the supplied cases. Implement the
   largest-first payment rule with the supplied validation and return contract.
3. Run the payment report. For the first case, check both payments yourself;
   confirm each sums to the target and compare their coin counts.
4. Check the other three outcomes. Distinguish “greedy got stuck” from “no exact
   payment exists.” State the limit of the optimality claim using the evidence.
5. Add focused tests for these cases, zero, unsorted/duplicate coins, unchanged
   input, and a few invalid inputs. Use the supplied reference; exhaustive search
   stays bounded to the issued small targets.
6. Commit a working Tuesday version. Record one useful pair question/decision in
   brief README notes, alongside your own contribution. No presentation or
   discussion-board review is required.

### Thursday — Reuse Repeated Answers

1. Follow the memoization lesson/demo. Compare the supplied uncached recurrence
   with the starter's equivalent recurrence before adding the cache behavior.
2. Add lookup, hit counting, and storage in calculate_cached. Preserve the
   recurrence's answer; do not replace it with a precomputed table or formula.
3. Set ENABLE_MEMOIZATION = True. The supplied driver now accepts --n, its default
   of 8, and --help. Parser construction is supplied and is not assessed.
4. Compare n=5: both answers are 5; uncached calls are 15; cached calls are 9,
   including 3 hits, with 6 distinct inputs saved. Explain what these categories
   count. A hit is already included in calls; do not add it again.
5. Check n=0, n=1, another independently known answer, and repeated fresh runs.
   Check rejection outside the wrapper's input contract. Ensure a cached zero
   is recognized. Tests may combine several checks in a small fixture.
6. Rerun Tuesday's checks. Keep one small before/after call comparison in output
   and a brief personal observation about reuse versus storage. More calls saved
   is evidence for these runs, not a measured speedup or universal performance claim.
7. Commit/push the completed shared work. Each member copies a complete runnable
   version to their own submission folder, runs it there, and adds personal README
   observations before submitting once.

## Evidence and Scope

Evidence stays in the readable payment comparison, small call/cache report,
focused test_assignment.py, and brief personal README. Shared code/results are
expected; each student's contribution/learning/assistance notes use their own words.
One useful pair question/decision is enough; no conversation transcript.

Tuesday uses the lab time remaining after the short AL06 completion/submission;
Thursday provides the full 120-minute lab. This is bounded practice in a
lower-pressure week, not two full applications. No timing benchmarks, trial
harness, large exhaustive runs, cache infrastructure, browser implementation,
mandatory extension, separate evidence report, or formal peer-review grade.
The optional Thursday LRN recognition demo is not a prerequisite.

## Run and Submit

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 main.py --help
py -3.14 test_assignment.py
```

Tuesday runs the payment stage without a parser prerequisite. Enable Thursday's
stage before using --n/--help. Use python if it selects your course interpreter;
run tests without -O. Enable **both test functions** before final submission.

Each student submits a complete week_05/AL07 folder in their own class repository:
main.py, test_assignment.py, the five supplied runtime modules, and personal
README.md. No imports from demos, AL06, or a partner's computer. Preserve AL06's
submitted folder. Daily progress uses commits, not separate Tuesday/Thursday folders.

Submit **your own class-repository URL and folder path** in Schoology, not the
shared repo or the course-materials repo. AI may explain, draft, debug, suggest
checks, or support understanding under the normal policy. Briefly identify help
and what you checked/changed/rejected; no manual-first gate or required AI use.

## Evaluation Focus

Existing MRS descriptors apply; classifications introduce no new weights.

### Primary

- T3 — Implement and test introductory algorithms using Python: greedy choices, explicit memoization, focused regression checks.
- T4 — Evaluate correctness, efficiency, and tradeoffs among algorithmic approaches: counterexample, unchanged answers, fresh-run evidence, qualified storage/work conclusions.
- C1 — Solve Problems: connect exact payment needs and repeated calculation to appropriate methods.
- C5 — Work Cooperatively: rotating roles, useful questions/decisions, shared progress and complete personal handoff.

### Secondary

- T1 — Frame problems and analyze algorithmic requirements: objective, constraints, local versus optimal claims, repeated subproblems.
- T2 — Select data structures and representations for algorithmic solutions: coin choices, dictionary keys/values, explicit per-run counter/cache state.
- T5 — Use observable evidence to explain algorithm behavior: readable comparisons and meaningful counter labels.
- T6 — Connect algorithmic thinking to AI, data systems, and responsible tool use: evaluate/disclose help and distinguish supplied from authored work.
- C2 — Communicate Clearly: brief individual strategy and contribution observations.

### Light / Incidental

- C3 — Work Productively: staged commits, handoffs, focused scope and runnable submission.
- C4 — Value Learning: respond to counterexamples, test failures, and feedback.
- C6 — Act Professionally: accurate attribution and personal repository submission.

### Not Assessed

None designated. Supplied parser/reference/display/counter plumbing is not a
separate implementation requirement. No additional peer-review artifact is required.
