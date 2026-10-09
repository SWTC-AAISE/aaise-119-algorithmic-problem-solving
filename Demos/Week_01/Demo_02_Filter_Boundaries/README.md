# Filter Boundaries

Week 1, Tuesday | Console-first Python demo

Identify equipment ready for a classroom loan; use purposeful tests to repair an inclusive battery boundary.

## Run

Keep `console_style.py` beside the application; it provides the reusable color helpers.
`main.py` is the uncluttered version; `main2.py` is the optional annotated companion.
Both use the same local styling module and demonstrate the same behavior.

```powershell
py -3.14 main.py
py -3.14 test_demo.py
```

Target: Python 3.14.6. No external packages, network, framework, or sibling imports. Use `python` instead of `py -3.14` where appropriate. Fixtures are embedded; no files are written. Tests are separate and reject `-O`.

Choose **1** for the useful report, **2** for the five-step teaching walkthrough, or **0** to exit. The walkthrough pauses four times for discussion. EOF or Ctrl+C ends input gracefully.

## Contract

Availability must be a Boolean; battery must be an integer from 0 through 100, not a Boolean. Unknown/missing/invalid values are excluded rather than silently converted. Exactly 50% qualifies. Records remain in inventory order and input data is not changed.

The intentionally incorrect rule is confined to the walkthrough. The ordinary report always uses the corrected rule.

## Report Results

```text
Ready to borrow
  E02 - Battery 50%
  E03 - Battery 51%

Not included
  E01 - Charge before lending
  E04 - Already on loan
  E05 - Battery or availability details need checking before lending
  E06 - Battery or availability details need checking before lending
  E07 - Battery or availability details need checking before lending

Result: 2 equipment item(s) ready to borrow.
```

The report also identifies the request and battery minimum. Empty or no-match input produces a readable no-results message. Ordinary output does not expose Boolean traces or test tables.

## Teaching Walkthrough

Predict 49%, 50%, 51%, unavailable, and unknown readings. Show the clearly labeled > defect, repair it to >=, and retain the other expectations.

English, pseudocode, and the relevant Python rule are shown explicitly. Expected outcomes are stated independently. Every function has a purpose docstring. Headings/results/cautions use console colors; Python examples use white on blue (`0;37;44`). Redirected output stays plain; `NO_COLOR` disables color.

[All daily demos](../../README.md)
