# Equipment Selection Synthesis: Workshop Laptop Loans

DEM-W08D01 | Week 8 synthesis demo | Planned delivery Tuesday, December 1

A loan-desk worker needs to know which requested devices are suitable for a
workshop. Show clear loan decisions, compare two lookup approaches under the same
policy, then adapt the policy when a longer workshop needs more battery.

## Run

From this folder:

```powershell
py -3.14 main.py
py -3.14 main2.py
py -3.14 test_demo.py
```

Use `python` if it selects your course interpreter. Target Python 3.14.6; verified
locally on 3.14.7. Standard library only, no packages, network, file writes or
sibling-demo imports. Run tests without `-O`.

Read `main.py` first. `main2.py` has the same functions and output with expanded
comments explaining the lecture concepts.

## Policy and Results

A device qualifies when it is a laptop, is available, and has battery **at least**
the stated minimum. All supplied fields are valid and equipment IDs are unique.
The records are fictional. Both approaches return one record or None per request,
in request order, without changing records or requests. Returned records reference
the inventory; the algorithms do not make independent copies of them.

| Request | Initial 50% policy: scan and index | Longer workshop: 80% policy |
| --- | --- | --- |
| E01 - Cedar laptop, 80% | Ready to loan | Still ready; exactly at the boundary |
| E02 - Maple laptop, 90% | Already checked out | Still checked out |
| E03 - Studio tablet, 95% | Request needs a laptop | Still not a laptop |
| E04 - Birch laptop, 50% | Ready; exactly at the boundary | Needs charging to meet 80% |
| E99 | Unknown ID | Still unknown |

The console displays these names and explanations, rather than raw lists of IDs
and None values. The middle report is explicitly labeled as a teaching comparison;
it changes the lookup approach while preserving the 50% policy. The last report
keeps the indexed approach and changes only the policy. Colors are reusable
presentation support; redirected output stays plain.

## Code Landmarks

- `eligible(row, minimum_battery)`: the common business rule.
- `scan_requests(rows, queries, minimum_battery)`: search the inventory separately for each requested ID.
- `indexed_requests(rows, queries, minimum_battery)`: build an eligible-device dictionary once for the group of requests, then use membership access.
- `equipment_data.py`: four named records and five requests.
- `equipment_display.py` and `console_style.py`: local presentation helpers.
- `test_demo.py`: independent expectations for both approaches and both code versions.

The lookup functions return the ordered result list directly. Explicit loops
make the two approaches visible without measurement infrastructure. Work/storage
reasoning stays qualitative.

## Work, Storage and Reuse

A scan can repeatedly visit earlier records for different requests. Preparing an
index visits the inventory first and uses extra dictionary storage, which may be
worthwhile for many requests. A tiny successful run does not establish that one
approach always has lower elapsed time.

This index contains only devices eligible under the supplied battery rule. Each
function call builds it afresh, so the 80% call does not reuse the earlier 50%
membership. If an application retained that eligible-only index, it would need to
refresh it when the relevant data or rule changes. An ID index containing **all**
records can be reused with a separate changing eligibility check; do not generalize
that every threshold change requires rebuilding every index.

## Verify and Explain

The tests check independently expected records/IDs, below/at/above boundaries,
unavailable/wrong-type/unknown devices, no matches, empty requests/inventory,
repeated request order, unchanged inputs and identical main/main2 output. Merely
agreeing with a second implementation is not the only evidence.

Ask: What changed for Birch, what stayed true for Cedar, and why? What does our
model leave out? Correct loan decisions under recorded battery/availability do
not prove that those records are current or that battery percentage predicts an
exact runtime. Connect that limitation to the current synthesis reading.

[All daily demos](../../README.md)
