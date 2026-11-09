# Greedy Counterexample

DEM-W05D02 | Week 5, Tuesday

Disprove universal optimality of largest-first coin selection.

Use main.py for the uncluttered code and main2.py for the same code with expanded
comments explaining validation, greedy choices, the supplied reference, and the
four cases. Both versions produce the same output.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Positive integer denominations, unlimited coins, minimum coin count; target is 0 through 12. None means no complete solution for that solver.

## Code Landmarks

- `validate`
- `greedy_change`
- `exhaustive_change`

The supplied reference_solver.py contains the top-level find_best_change helper.
It receives its inputs explicitly and returns its best completion to the caller;
there is no nested function or nonlocal state. Keep this module beside main.py.
Its exhaustive implementation is supporting code, not another algorithm students
must reproduce during the greedy lesson.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
GREEDY COUNTEREXAMPLE: minimize coin count, unlimited coins

Denominations=[1, 3, 4], target=6
  Largest-first: [4, 1, 1] (None means no complete greedy result)
  Exhaustive minimum: [3, 3]

Denominations=[3, 4], target=6
  Largest-first: None (None means no complete greedy result)
  Exhaustive minimum: [3, 3]

Denominations=[2, 4], target=3
  Largest-first: None (None means no complete greedy result)
  Exhaustive minimum: None

Denominations=[1, 5, 10], target=12
  Largest-first: [10, 1, 1] (None means no complete greedy result)
  Exhaustive minimum: [10, 1, 1]

4+1+1 uses 3 coins; 3+3 uses 2. Largest-first is not universally optimal.
A greedy failure also need not mean no solution exists.
```

## Explore

How can greedy failure coexist with an available complete solution?

[All daily demos](../../README.md)
