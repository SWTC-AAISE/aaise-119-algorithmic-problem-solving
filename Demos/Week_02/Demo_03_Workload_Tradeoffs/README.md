# Qualitative Workload Tradeoffs

DEM-W02D03 | Week 2 | Recognition-level Big-O

Discuss one-off versus repeated ID requests, index construction, reuse, and additional storage qualitatively. No measured winner or crossover is required.

## Run and Code Forms

```powershell
py -3.14 main.py
py -3.14 main2.py
py -3.14 test_demo.py
```

Keep both application files together. main.py uses explicit loops; main2.py
provides compact equivalents and imports the shared display. Brief separate AI
Explanation Prompt blocks name unfamiliar constructs. Supply the paired code
when requesting an explanation. Compact syntax does not imply better Big-O.

The examples are deliberately small, use unique synthetic equipment IDs, and
preserve query order and input data. Missing matches return None. Tests have
independently expected answers and counts; only the test run prints Checks passed.
Run tests without -O. No packages, network, parser, or timer is required.

## Scope

Explain what grows and recognize the corresponding Big-O label.
Exact counts illustrate tiny cases; no automated counting system, four-size
experiment, formal proof, average-case derivation, or benchmark report is required.
Diagnostic output is intentional for this algorithm lesson.


Target Python 3.14.6; available 3.14.7 and 3.12.10 are used for verification.
Actual measurements are parked for later. Archived measurement material lives
outside Demos and is not student Week 2 content.

[All daily demos](../../README.md)
