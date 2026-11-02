# Query Pipeline

DEM-W04D03 | Week 4, Thursday | Sorting simplification October 29, 2026

Compose eligibility, ordering, and Monday's familiar search contracts. Reuse functions rather than rebuild algorithms during integration.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Without the Windows launcher, use python main.py with the intended interpreter. Target Python 3.14.6; verified on installed Python 3.14.7 and 3.12.10, not exact 3.14.6. Standard library only; no packages, network, framework, sibling-demo imports, or generated files.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Documented Companion

[main2.py](main2.py) runs the same current logic and output, with expanded
comments on eligibility, shared records, view-relative results, and rebuilding
views. Both versions now use ordinary named-key sorting, with no comparator
adapter, nested comparator, or nonlocal counter. Generator visit totals are
explained alongside a separate handout with explicit-loop alternatives.
Run `py -3.14 main2.py` for this reading aid, or use main.py for uncluttered code.

## Modular Responsibilities

| Function | Responsibility |
| --- | --- |
| is_eligible(record, minimum_battery) | Arbitrary eligibility rule: availability and inclusive battery threshold |
| filter_available(records, minimum_battery) | Apply that predicate to produce a new selected list sharing record dictionaries |
| id_key(record), battery_key(record) | Select values for ordering/comparison |
| matches(value, target), compare_values(value, target) | Equality and ordered comparison, as in Monday's demo |
| linear_search / binary_search | Same callable-key arguments and (position, trace) result contract as Monday |
| order_for_search(records, key=id_key) | Return only a new list ordered by the named key; no comparator count |

Filtering is not ID lookup. Its predicate can combine rules; binary search requires an ordered key, not that predicate.

Display and search lists are separate shallow views of the same selected records. Positions must be resolved against the specific list passed to the search. None means absent; position 0 is valid. Filtering/reordering does not mutate the original list, but these are not independent deep copies of the records.

Both workflows share one filter pass. The ID sort is done once and reused across
queries; search-visit totals do not include its setup. Discuss that setup and
rebuilding qualitatively, without comparator instrumentation. Search visits are
not equal-duration operations; traces also allocate memory. No elapsed-time
superiority or crossover is claimed.

A changed battery threshold rebuilds selection and its search view; the key, equality, and search algorithms stay unchanged. The intentionally battery-ordered ID search violates its precondition.

## Syntax Support

- [Sorting keys and comparator adapters](../../../Resources-Handouts/Week_04_Sorting_Keys_and_Comparator_Adapters.md): simple named-key sorting first; adapter and nested-scope examples are reference only.
- [Generators and explicit alternatives](../../../Resources-Handouts/Week_04_Generators_and_Explicit_Alternatives.md): expressions, yield, consumption/exhaustion, and visit totals.

These handouts add no assignment deliverable. The former comparator-count
return value has been removed; callers now use `search_view = order_for_search(...)`.

## Expected Default Run

```text
QUERY PIPELINE: eligibility predicate -> views -> familiar search -> report
Reused search contract: (position in supplied view, trace); callable key
Eligible IDs: [3, 1, 2]
Battery-ordered display IDs: [3, 1, 2]
ID-ordered search view:      [1, 2, 3]
Invalid ID binary search in display, target 3: None
Same ID 3: linear position=0; binary position=2
Resolve positions against their own views: True
Correct search view, target 3: {'id': 3, 'battery': 20, 'available': True}
q=1: scan inspections=1; binary midpoint inspections=2
q=12: scan inspections=24; binary midpoint inspections=24
Filter scans 4 input records once; both workflows share that cost.
The ID search view is ordered once and reused; rebuilding it adds setup work.
Counts describe search visits, not equal-duration units or total timings.
Traces allocate memory for teaching; both workflows reuse one filtered view.
Changed battery threshold >=80: [1, 2]
ID 3 after the filter change: None
Filtering changes eligibility; it does not change the equality or search contract.
```

## Explore

Why are the linear/binary positions different for the same equipment? Which functions change for a new eligibility rule? What must change if the search key changes instead?

Each demo remains standalone. The additional Navigator APP-M4 recognition is separate from this daily demo.

[All daily demos](../../README.md)
