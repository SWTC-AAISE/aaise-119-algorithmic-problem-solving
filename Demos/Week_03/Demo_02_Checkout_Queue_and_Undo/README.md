# Checkout Queue and Undo

DEM-W03D02 | Week 3, Tuesday

Process checkout requests FIFO and reverse successful checkouts LIFO.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Documented Companion

[main2.py](main2.py) contains the same executable code and output as main.py,
with detailed comments connecting FIFO requests, LIFO history, local aliases,
and complete restoration to Tuesday's lecture and its four-row state example.
Use main.py for the uncluttered view or run `py -3.14 main2.py` for the documented version.

## Contract

Undo restores availability and places the consumed request at the queue front. Only successful checkout actions are reversible.

The inventory, waiting queue, and history have named local references inside
each operation. These names refer to the existing containers; they do not copy
them. History entries use `equipment_id` and `previous_available` fields rather
than unnamed tuple positions. Empty and denied requests do not add undo entries.

Introduce `deque()`, `append()`, `popleft()`, and `appendleft()` explicitly.
The history is a list: `append()` saves an action, `pop()` retrieves the most
recent action, and `undo[-1]` reads that latest entry without removing it.
This is checkout undo only, not a general transaction system.

Readable status reports replace raw container dumps. Console colors come from
the standalone Week 1 `console_style.py` helper; plain output remains complete.

## Code Landmarks

- `make_state`
- `enqueue`
- `checkout_next`
- `undo_checkout`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
EQUIPMENT CHECKOUT DESK

Initial requests
Equipment:
  E01 - Ready to borrow
  E02 - Ready to borrow
Waiting requests (next first):
  E01
  E02
No checkout available to undo.

E01: checked out
Equipment:
  E01 - On loan
  E02 - Ready to borrow
Waiting requests (next first):
  E02
Next checkout that can be undone: E01

E02: checked out
Equipment:
  E01 - On loan
  E02 - On loan
Waiting requests (next first):
  No requests waiting.
Next checkout that can be undone: E02

E02: checkout undone; request restored at front
Equipment:
  E01 - On loan
  E02 - Ready to borrow
Waiting requests (next first):
  E02
Next checkout that can be undone: E01

The most recent checkout is undone first; FIFO request order is restored.
```

## Explore

What prior state must undo save, and what does it restore?

[All daily demos](../../README.md)
