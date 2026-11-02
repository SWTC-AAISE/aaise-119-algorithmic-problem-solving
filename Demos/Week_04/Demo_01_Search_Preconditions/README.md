# Search Preconditions

DEM-W04D01 | Week 4, Monday | Refactored October 9, 2026

Show one deliberate progression: **key selection -> equality matching -> linear traversal -> ordered binary traversal**. The algorithms share criteria and result semantics; binary search adds an ordering precondition.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Without the Windows launcher, use python main.py with the intended interpreter. Target Python 3.14.6; verified on installed Python 3.14.7 and 3.12.10, not exact 3.14.6. Standard library only; no packages, network, framework, sibling-demo imports, or generated files.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Documented Companion

[main2.py](main2.py) runs the same logic and produces the same output, with
expanded comments on callable keys, linear/binary traversal, bounds, duplicate
semantics, compact syntax, and shared record views. Run `py -3.14 main2.py`
for the documented version, or use main.py for the uncluttered code view.

## Modular Contracts

| Function | Responsibility |
| --- | --- |
| id_key(record), model_key(record) | Select the field value; do not search |
| matches(value, target) | Decide equality; do not traverse |
| compare_values(value, target) | Return -1, 0, or 1 for comparable ordered values |
| linear_search(records, target, key=id_key) | Visit records until equality matches; input need not be sorted |
| binary_search(records, target, key=id_key) | Narrow an inclusive low/high interval; input must be ascending under the same key |

Both searches return (position, trace). None means absent, including empty input. Position is relative to the supplied view, not a permanent record ID. Reordering can change a position without changing which record matches.

The result contract allows any matching position. Linear search happens to return the first; binary search need not return the first duplicate. Equipment IDs in the fixtures are unique; model names can repeat.

A key is a callable selecting a value, not a field-name string or an arbitrary filter predicate. Changing from ID to model requires changing both the key and the ordering used for binary search. Fixture fields exist and values have compatible equality/ordering; malformed record validation is outside this focused demo.

Binary search does not scan to verify sorting on every call. Ordering is the caller's responsibility; an automatic linear preflight would change the query cost.

## Expected Default Run

```text
SEARCH SCAFFOLD: key -> match -> linear traversal -> ordered binary traversal
Shared contract: (position in supplied view, trace); None means absent

1. CRITERIA: id_key selects a value; matches defines equality
Input IDs: [3, 1, 2]
First record matches ID 3: True
First record matches ID 99: False

2. LINEAR: same criterion; no ordering requirement
Target 3: (0, [(0, 3)]) (position, visits)
Target 99: (None, [(0, 3), (1, 1), (2, 2)]) (position, visits)

3. BINARY: same criterion/result contract; ascending ID order
Search-view IDs: [1, 2, 3]
Target 3: position=2; (low, high, middle, value)
  (0, 2, 1, 2)
  (2, 2, 2, 3)
Target 99: position=None; (low, high, middle, value)
  (0, 2, 1, 2)
  (2, 2, 2, 3)
ID 3 is position 0 in the input, but position 2 in the search view.

4. PRECONDITION: matching alone cannot justify discarding half
Binary on [3, 1, 2], target 3: (None, [(0, 2, 1, 1), (2, 2, 2, 2)]) <- deliberate precondition violation
Changed key: model_key, target Laptop; models are already ascending.
Linear: (0, [(0, 'Laptop')])
Binary: (1, [(0, 2, 1, 'Laptop')])
IDs are unique; model names can repeat. Search contract permits any matching position.
An arbitrary filter predicate is not an ordered binary-search comparison.
```

## Continuity and Explore

Tuesday uses named callable keys to order records. Thursday preserves these search signatures and return semantics when composing the pipeline; each packet has its own independent copy of the teaching functions.

Ask: Which part stays unchanged when traversal changes? Why is equality alone insufficient to discard half the records? Why can position 0 and position 2 identify the same equipment in different views?

The traces allocate memory for observation; do not describe this traced implementation as a constant-extra-space binary-search implementation.

[All daily demos](../../README.md)
