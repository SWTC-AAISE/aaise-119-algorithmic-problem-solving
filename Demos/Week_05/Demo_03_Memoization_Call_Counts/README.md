# Memoization Call Counts

DEM-W05D03 | Week 5, Thursday

Compare uncached recurrence calls with fresh-cache memoization.

main.py uses top-level helpers with explicit dictionary state; main2.py is the
same code with expanded comments. Keep the supplied console_style.py beside them.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

Optional: `py -3.14 main.py --n 5` (n range 0-20; default 10).

Add `--trace` to show each recursive call, each cache hit, and the complete
cache after every new value is stored. For a short trace, try
`py -3.14 main.py --n 3 --trace`. Without `--trace`, output is unchanged.

## Contract

F(0)=0 and F(1)=1. Integer n is 0 through 20; every comparison starts with a fresh cache.

## Code Landmarks

- `validate`
- `calculate_uncached` and `calculate_cached`: top-level calculation helpers.
- `uncached_fibonacci`
- `cached_fibonacci`

The public functions create fresh state and preserve their result contracts:
`(result, calls)` and `(result, calls, hits, cache)`. Cache/counter dictionaries
are explicitly passed to recursive helpers; no nested function or nonlocal is used.
The optional `trace=True` argument to `cached_fibonacci` prints helper calls,
cache hits, and the cumulative cache after stores.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
MEMOIZATION: reuse an answer already calculated
F(10)=55
Answer with memoization: 55
Calls without memoization: 177
Calls with memoization: 19
Calls that reused a saved answer: 8
Distinct inputs saved in this run: 11

Both results use F(0)=0 and F(1)=1.
Every comparison starts with a fresh dictionary cache.
Calls include cache hits; counts describe work, not elapsed time.
```

## Explore

Which counts include cache hits, and which count newly computed subproblems?

Start the explanation with --n 5: result 5; 15 uncached helper calls versus
9 cached calls, including 3 hits, with 6 saved inputs. These counts exclude
validation, parsing, display, and the public wrapper calls.

See [Memoization, Caching, and Assignment Syntax](../../../Resources-Handouts/Week_05_Memoization_Caching_and_Assignment_Syntax.md)
for packed/unpacked assignment and the distinctions among this dictionary,
Python function-cache decorators, JavaScript application memory, browser HTTP
caching, the Cache API, and Web Storage. The web/library alternatives are
conceptual connections, not additional implementations for this demo or AL07.

[All daily demos](../../README.md)
