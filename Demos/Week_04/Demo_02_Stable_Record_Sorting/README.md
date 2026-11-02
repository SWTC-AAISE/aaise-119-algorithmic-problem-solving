# Stable Record Sorting

DEM-W04D02 | Week 4, Tuesday | Refactored October 9, 2026

Trace stable insertion sort and reuse Monday's **callable key** idea. Change the selected field without rewriting the sorting loop.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Without the Windows launcher, use python main.py with the intended interpreter. Target Python 3.14.6; verified on installed Python 3.14.7 and 3.12.10, not exact 3.14.6. Standard library only; no packages, network, framework, sibling-demo imports, or generated files.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Documented Companion

[main2.py](main2.py) runs the same logic and produces the same output, with
expanded comments on insertion steps, stable ties, counted units, shallow views,
compact display syntax, and the guided merge contrast. Run `py -3.14 main2.py`
for the documented version, or use main.py for the uncluttered code view.

## Syntax Support

- [Comprehensions and explicit loops](../../../Resources-Handouts/Week_04_Comprehensions_and_Explicit_Loops.md).
- [List slicing and concatenation](../../../Resources-Handouts/Week_04_List_Slicing_and_Concatenation.md): the guided merge's remaining inputs.
- [Unpacking return values and underscore](../../../Resources-Handouts/Week_04_Unpacking_Return_Values_and_Underscore.md): keeping only the result you need.

These are optional reading aids, not additional assignment deliverables.

## Contract and Landmarks

battery_key(record) and id_key(record) select values. insertion_sort(records, key) returns (ordered_copy, key_comparisons, right_shifts, trace). sorted(records, key=...) uses the same key contract.

The input list is not mutated; record objects are shared by the shallow list copy. Counts exclude final placements. Equal battery keys retain input order because the loop stops shifting on equality; an explicit ID tie-breaker is not the same stability claim.

merge_sorted is a supplied merge contrast, not a complete merge-sort implementation. Neither the callable key nor the merge contrast implies that Python's library sort uses this demo's algorithm.

For Thursday ID binary search, ordering by battery is not sufficient. Choose a separate ID-ordered search view using the same key as the search.

## Expected Default Run

```text
STABLE RECORD SORTING: ascending battery; input list is not mutated
Callable key contract: battery_key or id_key; the sorting loop stays unchanged.
Input: [('A', 70), ('B', 50), ('C', 70), ('D', 30)]
Insertion 1: ['B', 'A', 'C', 'D']
Insertion 2: ['B', 'A', 'C', 'D']
Insertion 3: ['D', 'B', 'A', 'C']
Result: ['D', 'B', 'A', 'C']
Key comparisons: 5; right-shifts: 4 (final placement not counted)
Equal-key A/C retain input order; an ID tie-breaker is not the same concept.
Changed key, same algorithm: ID order = ['A', 'B', 'C', 'D']
Guided merge contrast: [1, 4] + [2, 3] -> [1, 2, 3, 4]
```

## Explore

Why must equal keys stop shifting to preserve stability? What changes when id_key replaces battery_key, and what stays unchanged?

## Optional Browser Comparison

The existing example uses three separate layers: optional_js/index.html for structure, optional_js/styles.css for presentation, and optional_js/main.js for behavior. Styling remains external, not embedded in a style tag.

Open [the standalone HTML example](optional_js/index.html). No server or framework is needed; Python remains primary.

JavaScript Array.sort() mutates its array and returns it, unlike Python sorted(), which returns a new list. The copied-array example preserves original order; equal battery keys preserve A/C order. Shallow copies still share record objects. This browser example remains a sorting/mutation comparison, not a second search curriculum.

[All daily demos](../../README.md)
