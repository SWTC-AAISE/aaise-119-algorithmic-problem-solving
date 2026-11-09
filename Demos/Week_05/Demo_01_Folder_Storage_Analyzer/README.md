# Folder Storage Analyzer

DEM-W05D01 | Week 5, Monday

How much storage does a folder use, including every subfolder? This tool totals
the supplied Course Files example so someone can plan what to archive.
Recursion fits the structure: every subfolder asks the same question as its parent.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Use python if it selects your Python 3.14 interpreter. Keep the supplied modules
beside main.py. main2.py is the same application with expanded teaching comments.
The sample data is fictional; the program does not inspect your computer's files.

## Contract

A file record has type, name, and size_mb; a folder has type, name, and an items
list. Sizes are nonnegative whole MB, excluding booleans. Empty folders total
zero. Both algorithms return one numeric total, leave the input unchanged, and
expect a finite tree of these records. The supplied validate_item helper rejects
malformed individual records as each traversal visits them.

## Code Landmarks

- `recursive_total`
- `iterative_total`

The algorithms use the same original data. The iterative stack processes siblings
in reverse input order because it pops the last added item; the sum is unchanged.
Neither algorithm needs a fixed number of nesting levels or pre-flattened input.
Python recursion depth still limits how deep the recursive version can go.

## Supplied Modules

- folder_data.py: named sample records and validation.
- folder_display.py: readable indented folder report.
- console_style.py: reusable optional console colors.

Focus first on recursive_total and its returned subtotals; the display/helper
implementation is supporting code. [Sweigart Chapter 1](https://inventwithpython.com/recursion/chapter1.html)
provides this week's required function/call-stack reading.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
FOLDER STORAGE ANALYZER
How much space will Course Files need when we archive it?

Course Files/
  - notes.pdf (4 MB)
  Week 1/
    - slides.pdf (6 MB)
    Activities/
      - examples.zip (10 MB)

Total storage: 20 MB
Explicit-stack check: 20 MB

Every subfolder asks the same question: how much is inside me?
```

## Explore

Activities returns 10 MB, Week 1 returns 16 MB, and Course Files returns 20 MB.
Where does a caller pause while it waits for one of those subtotals?
What code would need to change if another folder surrounded Course Files?

An empty folder's loop has no items, so its total remains zero. A file supplies
the direct base-case answer. The iterative alternative keeps pending records in
a list stack rather than pending calls.

[All daily demos](../../README.md)
