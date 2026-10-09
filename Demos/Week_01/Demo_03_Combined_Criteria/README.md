# Combined Criteria

Week 1, Thursday | Console-first Python demo

Find laptops ready for class; distinguish a behavior-preserving refactor from a changed request.

## Run

Keep `console_style.py` beside the application; it provides the reusable color helpers.

```powershell
py -3.14 main.py
py -3.14 test_demo.py
```

Target: Python 3.14.6. No external packages, network, framework, or sibling imports. Use `python` instead of `py -3.14` where appropriate. Fixtures are embedded; no files are written. Tests are separate and reject `-O`.

Choose **1** for the useful report, **2** for the five-step teaching walkthrough, or **0** to exit. The walkthrough pauses four times for discussion. EOF or Ctrl+C ends input gracefully.

## Contract

Availability must be a Boolean; battery must be an integer from 0 through 100, not a Boolean. Unknown/missing/invalid values are excluded rather than silently converted. Exactly 50% qualifies. Records remain in inventory order and input data is not changed.

This request additionally requires a laptop. IDs must be nonempty text and equipment types laptop/tablet. The original request accepted either type. Named functions keep validation, selection rules, and presentation distinct.

## Report Results

```text
Ready to borrow
  E01 - Laptop - Battery 80%
  E04 - Laptop - Battery 50%

Not included
  E02 - Tablet available, but this class needs a laptop
  E03 - Already on loan
  E05 - Charge before lending
  E06 - Equipment details need checking before lending

Result: 2 laptop(s) ready for class.
```

The report also identifies the request and battery minimum. Empty or no-match input produces a readable no-results message. Ordinary output does not expose Boolean traces or test tables.

## Teaching Walkthrough

Predict E02 and E04 under the original request. Compare original/refactored answers, then add the laptop requirement. Only E02 changes; boundary and rejection expectations remain.

English, pseudocode, and the relevant Python rule are shown explicitly. Expected outcomes are stated independently. Every function has a purpose docstring. Headings/results/cautions use console colors; Python examples use white on blue (`0;37;44`). Redirected output stays plain; `NO_COLOR` disables color.

[All daily demos](../../README.md)

## Optional Browser Comparison

Open [the HTML example](optional_js/index.html). Structure, styling, and behavior remain separate in `index.html`, `styles.css`, and `main.js`. This optional, unchanged comparison uses a smaller validated fixture and JavaScript `filter()`/`every()`; it is not a line-for-line translation of the revised named-rule Python demo. Empty criteria select all in that browser example only, not an additional Python API requirement.
