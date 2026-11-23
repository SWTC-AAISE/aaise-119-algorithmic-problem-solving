# AL09: Explainable Resource Ranking and Integrity

Weeks 7-8 | Paired programming | One final personal submission

Calendar: stage 1 Monday, November 23; stage 2 Tuesday, November 24; stage 3
Monday, November 30. No class Thursday, November 26. Continue the same project
and partners after the break; keep the personal submission in week_07/AL09.
Deadline: posted by your instructor.

## The Problem

You want a short list of Python references for reviewing **queues and stacks**.
A general list of links is not enough: compare the supplied topic tags, show why
a reference matches, and adapt the shortlist when queues matter more.

Build a console application from fresh files with your assigned partner(s).
Use the supplied eight-resource catalog; do not reuse AL08 or reproduce the
Learning Resource Navigator. Resources and links are real; the tags are local
teaching judgments, not publisher ratings or measured educational quality.
These links are data for the application, not eight additional required readings.

The [Week 7 reading](../../Reading_Assignments.md) connects representation and
clustering concepts in Chapter 6 pp. 143-149 with recommendation types/limits in
Chapter 12 pp. 373-383. Our scoring formulas and snapshot helper are taught in
the daily lectures/demos. Chapter 14 remains the selected tie-in; no cipher or
security-system implementation is required.

## Supplied Files and Setup

Keep these five runtime modules beside your own main.py:

- resource_data.py: eight resource records, PROFILE, WEIGHTS, LIMIT, and LIMITATION_ID.
- resource_support.py: missing-tag policy, weight/limit checks, and canonical_bytes.
- resource_display.py: readable names, scores, matching topics, links, and change messages.
- app_runner.py: staged reports and independent stage-3 experimental copies.
- console_style.py: reusable console colors; redirected output remains plain.

Use README_Template.md for brief personal notes. Optional English-first scaffolds
are provided in [starter/main.py](starter/main.py) and
[starter/test_assignment.py](starter/test_assignment.py). Copy these two files
beside the five runtime modules above; run the copied files from that working
folder, not from inside starter/. Keep one active application and test file.

The starter labels stages 1 (Nov 23), 2 (Nov 24) and 3 (Nov 30). Set STAGE in
main.py and TEST_STAGE in test_assignment.py to the stage you are completing.
Both begin at 1; use 3 for the complete final submission. Later-stage functions
are not called early. Unfinished algorithms/tests raise NotImplementedError
until completed; that is expected. One small test example is supplied; complete
the remaining English checklists with your own assertions. You may instead
create your own files using the contracts below. No separate walkthrough or
support-use response is required. Instructor solution/ stays withheld until
grading ends.

Create main.py with a short purpose docstring for every function. Call the supplied
runner from your normal entry point; use only completed functions at each stage:

| Day | Runner Call |
| --- | --- |
| Monday, Nov 23 | run(1, shared_count, jaccard) |
| Tuesday, Nov 24 | run(2, shared_count, jaccard, rank_resources) |
| Monday, Nov 30 | run(3, shared_count, jaccard, rank_resources, catalog_digest) |

Import run from app_runner. Change the call as work progresses; maintain one
application rather than three daily copies. STAGE is optional if you prefer a
switch like earlier assignments. The final run must execute stage 3.

## Data and Scoring Contract

PROFILE is {"queues", "stacks"}; WEIGHTS is {"queues": 4}; LIMIT is 2.
Each resource has a unique string id, title, url, and a tags list. Keep the supplied
fixture unchanged. Missing or None tags in a controlled test mean an empty set.
Tag comparison is exact; repeated tags count only once.

- shared_count: size of the intersection.
- Jaccard: intersection size / union size; return 0 when the union is empty.
- Weighted similarity: matched tag weight / all distinct union tag weight.
- Unspecified tag weights are 1. An empty or all-zero-weight union scores 0.
- Weights are finite nonnegative numbers; Boolean values are not weights. Use supplied validate_weights.
- Rank by descending score, then ascending ID for exact ties; apply k after sorting.
- k is a nonnegative integer. Zero returns no results; a larger-than-catalog k returns all available records. Use supplied require_limit.
- The profile is a set of preferences, not a catalog record. There is no self ID to exclude. Do not discard an otherwise valid exact tag match.
- Preserve resources, their nested tags, profiles, and weight dictionaries.

### Functions You Write

| Function | Return Contract |
| --- | --- |
| shared_count(left, right) | Integer count of distinct shared tags. |
| jaccard(left, right) | Numeric overlap/union score with the stated empty policy. |
| weighted_similarity(tags, profile, weights) | (score, contributions, union_weight); contributions maps each matching tag to its weight. |
| rank_resources(resources, profile, weights, k) | Ordered list of at most k new result dictionaries, with the fields below. |
| catalog_digest(resources) | Printable SHA-256 hexadecimal digest of supplied canonical_bytes(resources). |

Each ranked result contains id, title, url, score, matched (sorted matching tags),
contributions (matching-tag weights), and union_weight (denominator).
An empty weights dictionary gives equal-weight Jaccard ranking.
Use named helpers if useful; a lambda, comprehension, generator, class, or
nested function is not required.

For catalog_digest, use hashlib's standard library implementation. The supplied
helper selects ID, title, URL and unique sorted tags, sorts records/JSON keys,
and produces consistently formatted UTF-8 bytes. Record/tag ordering does not
change that snapshot; a title or URL edit does. Extra fields outside the contract
are not checked. You do not implement another serializer or cryptographic algorithm.

## Build Across the Meetings

### Monday, November 23 - Represent and Compare

1. Set up a fresh shared project with the supplied modules. Each member keeps their own class repository separate.
2. Inspect the records and the queues/stacks profile. Explain briefly what the tags represent and one thing they omit.
3. Write shared_count and jaccard using sets and explicit steps. Call the supplied runner at stage 1.
4. Display the resource names, shared-tag counts, scores and matched topics using the supplied report.
5. Independently check a small example: a queues/collections record versus the queues/stacks profile has one shared tag and three distinct union tags, so its Jaccard score is 1/3.
6. Add focused checks for repeated tags, no overlap, empty inputs, and the chosen missing-tag policy. You may use tiny fictional records for boundary tests; do not alter the real fixture.
7. Commit/push progress at role changes and keep short personal work notes for your final README.

You do not need top-k or weighted ranking before Tuesday's instruction.
Monday's output can remain in catalog order; the runner supplies that presentation.

### Tuesday, November 24 - Rank, Resolve Ties, and Change a Preference

1. Continue the same project. Implement weighted_similarity and rank_resources.
2. First use equal weights. Score all candidates, sort by score/ID, then keep the top two.
3. Verify the baseline shortlist: **LR013, LR002**. LR002 and LR003 both score 1/3; ascending ID selects LR002 even though LR003 appears earlier in the supplied data.
4. Check that reversing input order preserves the ranked result. Increase k to three in a test to reveal both tied candidates; do not slice the input before sorting.
5. Apply queues weight 4 and default weight 1 for other tags. Independently check the numerator and union denominator. Verify the shortlist becomes **LR013, LR003**.
6. Test all-one-weight parity with Jaccard, zero-total weight, empty catalog, missing tags, k=0, and k larger than the catalog. Use the supplied checks for invalid weights/limits; no new validation framework.
7. Run stage 2. Explain one changed recommendation through its matched contributions, then commit/push and hand off roles.

The optional music-demo tag filter/CLI is not an additional requirement here.
The assignment's full eight-record catalog is eligible. Do not add a search UI,
model training, or clustering implementation.

### Monday, November 30 - Explain Limits and Check a Snapshot

1. Re-run your scoring/ranking checks before continuing. Write catalog_digest using the supplied canonical_bytes helper and the standard-library hash.
2. Run stage 3. The runner creates an independent copy with LR013's tags removed. Predict the new baseline top two, then verify **LR002, LR003**. The reference page has not changed; its represented topics have.
3. In your tests, independently check that controlled missing-tag case and that the original catalog remains unchanged. The runner's display is evidence, not a substitute for an expected-result test.
4. Observe the runner's separate title-only edit, starting again from the original catalog. Confirm the metadata digest changes while recommendation IDs, order, and scores stay the same. Test this behavior.
5. Test that reversing record/tag order preserves the digest. Briefly state what fields were checked and why a match does not prove trustworthy sources or good recommendations.
6. Commit/push the shared working project. Each member copies the complete runnable app and tests into their own class repository's week_07/AL09 folder.
7. Add your own brief README observations, contribution and assistance notes. Run the copied app/tests, commit/push, and submit your own repository URL and folder path in Schoology.

The two controlled edits are independent. The runner supplies deepcopy and display
mechanics; you interpret and test the results. A matching digest compares the
selected metadata against a trusted local reference, not the remote web page
contents. It is not encryption, an authenticity guarantee, or a quality score.

## Work Together and Submit

Use the [paired programming/submission guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md).
Work in Zoom breakout rooms; rotate driver/navigator about every twenty minutes.
Commit/push before the next driver pulls. Include the trio member in meaningful
coding/checking/questions. Ask for instructor help through Zoom; schedule your
own Zoom session if extra joint time is needed.

Submit main.py, test_assignment.py, the five supplied modules, and your personal
README.md together. No imports from another assignment, a daily demo, the LRN, or
a partner's machine. Keep earlier assignment folders complete.

Run from the final personal folder:

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use python if it selects your course interpreter. Run tests without -O.
Submit once at the posted deadline using **your own class-repository URL**,
not the shared pair or course-materials repository.

## Evidence, AI Use, and Workload

Evidence stays in useful output, focused tests, and one personal README summarizing
all three stages. Do not create a separate README or submission for each meeting.
No pseudocode, essay, separate evidence report, formal peer-review post, URL
research, benchmark, full LRN clone, or extra UI is required.

AI can explain concepts, draft, debug, suggest checks, and support understanding.
Clarify the intended behavior and independently reason about small expectations.
Test the resulting code and justify actual assistance, including what you checked,
changed, or rejected. A completed manual implementation is not a prerequisite;
not using AI does not lower the grading ceiling.

Plan around 70 lab minutes November 23, 120 on November 24, and 70 on November 30.
If needed, up to 50 minutes of December 1 lab can support remaining AL09 checks and
personal packaging. This preserves the original 310-minute total allowance across
the scheduled labs; no class is held on November 26. These are unpiloted allocations,
not completion guarantees. The instructor posts the actual deadline. If ahead, strengthen tests or explanations;
new features are not required for full credit.

## Evaluation Focus

Existing MRS descriptors apply; these classifications add no new weights.

### Primary

- T2 — Select data structures and representations for algorithmic solutions: sets, profiles, named result dictionaries and the meaning/limits of tags.
- T3 — Implement and test introductory algorithms using Python: overlap, Jaccard, weighted ranking, digest usage and focused expected-result tests.
- T4 — Evaluate correctness, efficiency, and tradeoffs among algorithmic approaches: compare scoring rules, tie policy, weighted outcomes and missing-data limitations; no timing experiment.
- T5 — Use observable evidence to explain algorithm behavior: readable rankings, matched contributions, changed/unchanged comparisons and tests.
- T6 — Connect algorithmic thinking to AI, data systems, and responsible tool use: content-based recommendations, qualified digest claims and justified/validated assistance.
- C1 — Solve Problems: turn the study need into scoring, ranking and a controlled adaptation.
- C5 — Work Cooperatively: rotating roles, useful questions/checks, commits and shared-to-personal handoff.

### Secondary

- T1 — Frame problems and analyze algorithmic requirements: inputs, result contracts, profile, weights and assumptions.
- C2 — Communicate Clearly: brief personal reasoning connecting results to the selected rules.

### Light / Incidental

- C3 — Work Productively: staged progress, usable commits and a complete runnable submission.
- C4 — Value Learning: apply reading, examples, feedback and tests.
- C6 — Act Professionally: accurate attribution, clear ownership and responsible submission.

### Not Assessed

None designated. Supplied serialization, copying, formatting and input-validation
plumbing are not independent implementation requirements. No extra collaboration
or support-use document is required.
