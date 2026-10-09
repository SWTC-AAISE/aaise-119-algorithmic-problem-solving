# AL01: Ticket Rules and Follow-Up

Week 1 | Paired programming | Individual submission
Deadline and submission directions: provided by your instructor.

## Problem

The help desk needs a list of open tickets and a list requiring follow-up.
Build a console application that produces both lists, flags unusable records,
and adapts when the follow-up policy changes.

This is one progressive assignment. Start Monday; add each stage after its lecture and demo.

## What You Will Practice

- Turning a practical request into working selection rules.
- Validating data and testing boundaries.
- Repairing a defect, changing a policy, and refactoring without unintended changes.
- Presenting useful results and explaining what you learned.

## Supplied Data

Use `ticket_data.py`: 12 fictional tickets, including three invalid records.
Keep the supplied data unchanged; use small additional lists for focused tests.

| Field | Accepted value |
| --- | --- |
| id | Nonempty text; not whitespace-only |
| status | open or closed |
| category | software, network, or access |
| age_days | Integer >= 0; not a Python Boolean |
| priority | low, normal, or high |

All fields are required. Exclude invalid records and report what needs checking.
Do not guess or convert their values. A valid ticket that does not match a rule
is not an invalid record.

## Build Across the Week

| Day | Task |
| --- | --- |
| Monday | Build validation and a view of valid open tickets. |
| Tuesday | Add follow-up v1: valid, open, and at least 2 days old. Test the boundary and repair the supplied defect below. |
| Thursday | Change follow-up to v2: valid, open, at least 2 days old, and either high priority or access category. Make one small refactor and rerun your tests. |

The Thursday alternatives cannot bypass validity, open status, or minimum age.
The open-ticket view stays unchanged.

Tuesday's isolated defect:

```python
def meets_follow_up_age(age_days):
    """Check a previously validated age; this example contains a defect."""
    return age_days > 2
```

Predict the result at exactly 2 days, run the example, and repair it to match
the policy. Keep this teaching defect out of the normal application.

A policy change may change results. A refactor changes code organization while
preserving the current policy's results. Keep one final application; briefly
record a changed and an unchanged result as you move from v1 to v2.

## Program Requirements

- Implement `select_open_tickets(records)` and `select_follow_up(records)`.
  Each returns `(selected, issues)`: matching records and readable invalid-record messages.
- Keep results in input order and do not change input records.
- Separate validation, selection rules, and presentation into named functions
  with short purpose docstrings.
- Display the request/current policy, selected IDs and useful fields, a count,
  and any records needing checking.
- Give a clear message when no tickets match. Do not use dictionary dumps or
  technical traces as normal output.

One application file is enough. Menus, color, classes, sorting, benchmarking,
file parsing, APIs, and a web version are not required.

## Getting Started and AI Use

Begin with a brief statement of what each list should do; this can be a few
sentences or a conversation with your instructor. No pseudocode or formal
planning document is required.

You may use AI to explain, draft code, debug, or refactor within the stated task.
Provide your intended behavior and constraints, review its contribution, and test
the result. A complete manual implementation is not a prerequisite. Try to
identify the mismatch before asking for debugging help. For tools that edit files,
ask for an explanation/proposed change and approve the scope before editing.

Do not ask AI to invent your reflections or evidence, and do not submit code you
cannot explain. Predict focused test outcomes from the rules rather than using
the implementation to determine its own expected answers. AI use is optional;
briefly record what it helped with and what you checked or changed.

The [thinking guide](AL01_Thinking_Guide.md) and optional `starter/` files
provide a full-English M / T / Th walkthrough derived from a simple working
approach. Optional `starter/console_style.py` supplies reusable presentation
colors; copy it alongside your program if you choose to import it. The starter
is not a completed solution or a required
architecture. Use it, ask AI for bounded implementation help, or build your own
program with the same selector interfaces. All approaches have the same grading ceiling.

The [standard AI policy](../../PreCourse_Setup/Standard_Student_AI_Use_Policy.md) applies.
Individual understanding checks use no generative AI.

### Optional Support

Use the [AL01 Thinking Guide](AL01_Thinking_Guide.md) if you need help turning
the task into ordered steps. It is guidance, not a finished submission.
If you use it, briefly note in your README what pattern helped and what you
still had to decide or adapt. A few sentences within your normal notes are enough.

The single starter file has separate Monday, Tuesday, and Thursday sections.
Wait for the corresponding day's instruction before starting its section.
Keep developing one `main.py`, commit your progress, and submit once.

## Check Your Work

Keep executable checks in `test_assignment.py`. Use this coverage checklist,
not a required test count:

- Ordinary matching and nonmatching tickets.
- Ages below, exactly at, and above 2 days.
- Invalid/missing fields, including Boolean ages.
- Empty input and valid input with no matches.
- Thursday alternatives: high priority and access category each qualify when
  mandatory conditions hold; neither admits closed or too-young tickets.
- A result deliberately changed by v2 and a preserved result.
- Unchanged open-ticket behavior, input order/data, and final-policy results
  before/after your refactor.

Use independently chosen expected results. Tests supply the evidence; no duplicate
expected/actual table, screenshots, or separate worked-decision essay is required.

## README and Submission

### Work Together

Follow the [Paired Programming and Assignment Submission Guide](../../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md).
Develop one application in a shared public assignment repository, with your
partner(s) and instructor as collaborators. Work in Zoom breakout rooms during
lab, switch driver/navigator roles about every 20 minutes, and save, commit,
push, and pull at handoffs. In a trio, rotate all three through the driver role.
Use Zoom chat to request instructor help; independently schedule Zoom sessions
if additional joint work is needed outside lab.

AL01 has no separate presentation, Schoology discussion, or formal peer-review
writeup. Questions and checking each other's work are part of paired development.

### Submit Individually

Keep `main.py`, `ticket_data.py`, `test_assignment.py`, and `README.md`
together in your submission folder. Adapt [the README template](README_Template.md).

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Use `python` instead if appropriate for your course interpreter.
No external packages are required. Run tests without `-O`.

Append short README notes as you work: observations, debugging challenges,
changes, and learnings. Include the boundary repair, one changed/preserved
policy result, and your refactor outcome within those notes. Bullets are fine;
do not repeat the supplied schema or write a second specification. Add an
assistance note and leave the Instructor Comments section for grading.

Before submitting, check that the application runs, both lists follow the final
rules and tests pass. Each member copies the agreed complete solution and any
support modules into the designated `week_nn` assignment folder in their own
class repository. Do not copy the shared repository's `.git` folder. Add your
own README notes, partner names, shared repository link, and brief contribution
note. Run the copied application/tests, then commit and push your own submission.

Submit **your own class repository URL in Schoology, not the shared repository
URL**, and identify the assignment folder. Submit once after the final stage;
daily work is recorded through commits. Follow the instructor's posted deadline
and folder directions.

## Evaluation Focus

This assignment uses the existing MRS descriptors and the emphasis below.

### Primary Rubric Focus

- **T1 - Problem Framing and Algorithmic Analysis:** selection rules match the problem and can be explained.
- **T3 - Algorithm Implementation and Testing:** working validation/selection, purposeful tests, and repair/regression.
- **T5 - Observable Algorithm Behavior and Communication Evidence:** readable results, executable test evidence, and concise change observations.
- **C1 - Solve Problems:** identify the needed decisions, diagnose failures, and adapt the solution to the revised policy.
- **C5 - Work Cooperatively:** contribute actively in paired development, rotate roles, make clear handoffs, and help verify the joint work.

### Secondary Rubric Focus

- **T2 - Data Structures and Representation:** correctly access and process the list of ticket dictionaries, preserve order, and avoid unintended input changes.
- **T6 - AI/Data Foundations and Responsible Tool Use:** follow AI permissions, evaluate and verify contributions, and disclose assistance. Choosing not to use AI is not penalized; responsible decisions and explainable work are the focus.
- **C2 - Communicate Clearly:** understandable output and brief README learning notes.

### Light / Incidental Focus

- **C3 - Work Productively:** make progress through the staged work and maintain runnable, organized submission files.
- **C4 - Value Learning:** respond to feedback and use testing/debugging observations to improve the work.
- **C6 - Act Professionally:** follow submission expectations, acknowledge contributions honestly, and take responsibility for the submitted work.

### Not Assessed

- **T4 - Correctness, Efficiency, and Tradeoff Evaluation**

Not Assessed categories are N/A and receive automatic full points under the
instructor's practice. Emphasis labels do not introduce new weights.
Optional scaffolding or choosing not to use AI does not reduce the grading ceiling.
Assess these categories through the work, brief explanations, and observed process;
no additional essays or tracking documents are required. AL01 assesses paired
cooperation, not a separate formal peer-review activity.
