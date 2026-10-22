# Inventory Representations

DEM-W03D01 | Week 3, Monday

Compare list scans, keyed dictionaries, and set membership.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Duplicate IDs are rejected. Indexed records are independent flat copies; this is not a general nested deep-copy guarantee.

## Code Landmarks

- `build_index`
- `scan_lookup`
- `available_ids`: explicit availability filtering, with the original compact
  expression retained as a commented comparison.
- `display_record`: readable equipment results; presentation is separate from lookup.

## Set Foundation

A set stores unique values and answers membership questions. For these examples
its members are equipment-type strings, not entire record dictionaries.

- `set()` creates an empty set; `{}` creates an empty dictionary.
- `types.add("laptop")` adds a type; adding it again does not create a duplicate.
- `"camera" in types` checks membership; sets have no numbered positions.
- `types.discard("camera")` removes it if present, without failing if absent.
- `remove()` differs from `discard()` by raising `KeyError` if the value is absent.

Monday's retained expression is `types = {row["type"] for row in rows}`. It
collects each type once, just as this explicit loop does:

```python
types = set()
for row in rows:
    types.add(row["type"])
```

Optional AI explanation prompt: "Explain this set comprehension using the loop
above. Why do two laptop records produce only one laptop value? Explain why
sorting the display does not make the set itself an ordered sequence."

`build_index` copies each flat record intentionally. Week 2's index referred to
the originals. Neither behavior is automatic merely because a dictionary is used.
Nested snapshot copying is Thursday's separate comparison.

Colors use the same standalone `console_style.py` helper as Week 1. Redirected
output and `NO_COLOR` use plain text; color never changes the results.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
EQUIPMENT LOAN DESK
Find equipment E03
List search:
  E03 - Laptop - On loan
  Records checked: 3
ID index:
  E03 - Laptop - On loan

Equipment types we carry
  Laptop
  Tablet
Camera requests: we do not carry this type.

After checking out E01 in the working index
Working record:
  E01 - Laptop - On loan
Original record, kept separately:
  E01 - Laptop - Ready to borrow
  This index uses flat copies; Week 2's index shared its records.

Ready to borrow now
  E02 - Tablet - Ready to borrow

New record not added: equipment ID E01 is already in use.
```

## Explore

Which operations still require filtering after an ID index exists?

[All daily demos](../../README.md)
