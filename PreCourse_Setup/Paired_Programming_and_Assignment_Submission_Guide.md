# Paired Programming and Assignment Submission

Use this guide when an assignment is designated as paired programming.
Partners rotate per assignment, not on a fixed two-week schedule.

## 1. Work Together

### Set Up the Shared Repository

- One member creates a public GitHub repository for the assignment.
- Add the other member(s) and your instructor as collaborators. Accept invitations before starting.
- Each member clones the shared repository to their computer.
- Keep this separate from your individual class repository. Do not add partners to your class repository.

### Meet and Rotate

During scheduled lab time, work in your assigned Zoom breakout room.
The instructor visits rooms on a rotating basis as they deem appropriate.
Use the Zoom chat interface at any time to request help or instructor review;
you do not need to wait for a visit. If your breakout-room chat does not reach
the instructor, use Zoom's Ask for Help control.

If additional collaboration is needed outside lab, arrange your own meeting
time and independently schedule a Zoom session with your partner(s).

- **Driver:** shares their screen, edits the code, and runs the application/tests.
- **Navigator:** follows the work, asks questions, checks requirements, and suggests tests or improvements.
- Switch roles about every **20 minutes**, at a sensible stopping point.
- In a trio, rotate all three through the driver role; the other two actively navigate and review.
- Only the current driver edits shared project files. Do not split into simultaneous independent editing.
- When using permitted AI help, review proposed changes together before the driver applies them.

### Hand Off the Latest Work

The outgoing driver saves, runs available checks, commits with a meaningful
message, and pushes. Explain anything unfinished or failing before switching.
The incoming driver pulls the latest shared work before editing, then shares
their screen. Use your Git interface or these commands in the shared repository:

```powershell
# Outgoing driver: after saving and checking the work
git status
git add <files-you-changed>
git commit -m "Describe the change"
git push

# Incoming driver: before editing
git status
git pull
```

Replace `<files-you-changed>` with actual filenames. If there are no changes,
no new commit is needed. Do not pull over uncommitted local changes or start
editing after a failed push/pull. Ask the instructor for help rather than
discarding changes or force-pushing. Both members should participate in coding,
testing, and understanding the solution; commit counts alone do not measure participation.

## 2. Copy and Submit the Final Work

For class-repository setup and the standard Schoology submission steps, use the
[GitHub Submission Guide](GitHub_Class_Repository_and_Submission_Guide.md).

1. Agree on the finished shared version. Run the application/tests, then commit and push any final changes.
2. Each member pulls that version and copies the complete application files and dependencies into the appropriate `week_nn` assignment folder in their **own class repository**. Do not copy the shared repository's `.git` folder; hidden history is not part of the submission.
3. Keep the shared code consistent at submission. In your own README, identify the partners and shared repository, briefly describe your contribution, and append your own reflections, observations, debugging challenges, learnings, and AI-use note. Leave Instructor Comments for grading.
4. Run the copied application and tests from the destination folder to confirm it is complete and does not depend on files left in the shared repository.
5. Commit and push the submission to your own class repository. Confirm the files are visible on GitHub and your instructor remains a collaborator.
6. Submit **your own class repository URL in Schoology, NOT the shared repository URL**. Identify the week/assignment folder in the submission message so the instructor can find it.

Each student submits individually, even though the application was developed
together. For a later graded iteration, copy the previous solution into a new
designated folder; leave earlier submitted versions intact. Daily progress
within one assignment stays in the same working application with successive commits.

### Individual Work With Peer Review

Some assignments may instead specify individual implementation with peer review.
Follow that assignment's instructions; a shared repository is not automatically
required. Individual reflections do not change a paired assignment into a different mode.
