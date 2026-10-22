# State Consistency

DEM-W03D03 | Week 3, Thursday

Expose stale references and distinguish shallow aliases from independent snapshots.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Repair removes pending IDs missing from inventory. Deep copies are independent, not immutable.

Both repair functions use ordinary loops. `repair_queue` creates a new deque;
it does not consume or rewrite the original waiting queue. The copy comparison
separates building a list of shared records, taking a deep snapshot, and changing
the live inventory. `deepcopy()` is a deliberately introduced library operation,
not an algorithm students must reimplement.

Colors use the standalone Week 1 `console_style.py` helper. Availability labels
carry the result even when color is disabled or output is redirected.

## Code Landmarks

- `stale_ids`
- `repair_queue`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
EQUIPMENT SERVICE UPDATE
Waiting requests before the service update:
  E01
  E02

E02 has been removed from inventory.
  Request needs attention: E02 is no longer in inventory.
  Closed request for removed equipment: E02
Waiting requests after repair:
  E01

E01 has now been checked out.
  Current inventory: E01 - On loan
  New list, same record: E01 - On loan
  Independent saved snapshot: E01 - Ready to borrow
  The saved snapshot is independent, not read-only.
```

## Optional Compact-Code Reference

The former repair expression was:

```python
return deque(equipment_id for equipment_id in pending if equipment_id in inventory), removed
```

It filters IDs with a generator expression, uses those IDs to construct a deque,
and returns that deque together with the removed IDs. The explicit loop in
`main.py` does the same work in separate steps. This syntax is not required.

Optional AI explanation prompt: "Explain the generator expression and two-value
return above by comparing them with repair_queue's explicit loop. Show why both
preserve valid request order and leave the original queue unchanged."

## Explore

Why does copying the outer list not preserve the previous record values?

[All daily demos](../../README.md)
