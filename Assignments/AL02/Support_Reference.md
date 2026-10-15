# AL02 Supplied Support

## Optional Starter Setup

Copy starter/main.py and starter/test_assignment.py into your working folder
beside catalog_data.py and growth_examples.py. Adapt README_Template.md as README.md.
Use one main.py all week; no nested folder should separate imports.
Start a fresh shared project with the new pair; no AL01 code is needed.

The starter suggests an approach in plain English. Unfinished functions and
tests raise NotImplementedError. Initial main.py displays only a starting message;
it does not claim that the application is complete. Support is optional and
adds no writing requirement or reduced grading ceiling.

## Small Data

```python
from catalog_data import BOOKS, validate_book_ids

records = BOOKS
validate_book_ids(records)
```

IDs are B1 through B4, with title and author for each book. Records are a small
local teaching catalog, not an operational library database. Empty input is accepted;
blank/missing/duplicate IDs are rejected. Write your own three lookup functions.

## Growth Examples

growth_examples.py contains four deliberately small functions. Inspect the code,
identify the pattern, and record its Big-O label with one short reason.

You can run first_id, all_ids, and ordered_pairs on BOOKS, or call
halving_sizes(8), to see results. They are illustrations, not a benchmark harness.
You do not need to rewrite these supplied functions or add them to your app's UI.

Keep run/display calls inside the usual main guard so importing main.py for
tests does not start prompts or application output.

## Boundary

No timer, median, repeat-trial system, counter function, four-size experiment,
generated evidence file, or measured-winner requirement. Tiny manual traces can
help recognition; they must not become another compulsory reporting system.
