# Equipment Loan Desk

DEM-W01D01 | Week 1, Monday | Equipment Request Contract

A student needs a laptop for class. The equipment desk needs to know which laptops are available and sufficiently charged, without lending equipment whose details need checking.

## Run

Keep `console_style.py` beside the application; it provides the reusable color helpers.
`main.py` is the uncluttered version; `main2.py` is the optional annotated companion.
Both use the same local styling module and demonstrate the same behavior.

From this demo folder:

```powershell
py -3.14 main.py
```

Without the Windows Python launcher, use `python main.py`. Target: Python 3.14.6; tested on Python 3.14.7 and 3.12.10. No packages, network, web framework, or sibling-demo imports are required. This is a report using a small fictional inventory, not a live checkout system. It does not change availability or write files.

The opening menu offers **1** for the normal report, **2** for the teaching walkthrough, and **0** to exit. The walkthrough has five Enter-to-continue pauses for discussion and returns to the menu after its final report. Invalid menu choices can be retried; interrupted or closed console input exits gracefully.

## Console Color

In an ANSI-capable terminal, cyan identifies headings, green marks ready equipment and matching expectations, yellow marks cautions, and red marks the intentional failed comparison. Python examples use normal-style white text on a blue background (`0;37;44`) for clearer screen sharing. Other colors retain the terminal's existing background; every colored segment resets afterward. Text labels remain meaningful without color.

Redirected output and `TERM=dumb` use plain text automatically. To disable color in PowerShell:

```powershell
$env:NO_COLOR = "1"
py -3.14 main.py
Remove-Item Env:NO_COLOR
```

Even an empty `NO_COLOR` environment variable disables color. Use an ANSI-capable terminal such as Windows Terminal; if an older console shows escape characters, disable color. The expected report below is the plain-text equivalent.

Student references: [ANSI color chart generator](console_color_generator.py) and its [sample output image](console_color.png). These supplied files are preserved unchanged. The generator intentionally prints the complete chart; it is not imported by the application.

## Request Rules

- Include laptops that are available and have at least 50% battery. Exactly 50% qualifies.
- Require nonempty equipment ID/type, boolean availability, and an integer battery percentage from 0 through 100. A Python boolean is not a battery reading.
- Exclude incomplete or invalid records and explain that their details need checking. Missing battery does not mean 0%.
- Keep inventory order and leave the original records unchanged.

## Expected Report (Menu Option 1)

```text
Equipment Loan Desk
===================
Request: A laptop available to borrow today
Minimum battery: 50%

Ready to borrow
  E01 - Laptop - Battery 80%
  E04 - Laptop - Battery 50%

Not included
  E02 - Already on loan
  E03 - Not a laptop; this request is for a laptop
  E05 - Battery not recorded; check before lending

Result: 2 laptops meet the request.
```

## Teaching Walkthrough (Menu Option 2)

1. Begin with an ambiguous equipment-loan request.
2. Revise it into precise eligibility and data-quality rules.
3. Connect plain English, pseudocode, and the actual Python battery function.
4. Observe an intentionally incorrect `>` rule reject a valid 50% laptop.
5. Correct the rule to `>=` and compare independently stated expectations with actual application results.
6. Finish with the useful loan-desk report.

The initial comparison uses only valid, available laptops at 49%, 50%, and 51%, isolating the boundary mistake. The corrected comparison also checks equipment on loan, a different equipment type, and unknown battery. The deliberately incorrect rule is never used for the standard report.

## Explore and Check

For an instructor-led variation, change the call inside menu option 1 from `show_report()` to `show_report(minimum_battery=80)`. Predict the result before choosing 1; only E01 qualifies. At 100%, no laptops qualify. Restore `show_report()` afterward. No parser or separate technical trace mode is used.

Regression verification is separate from the ordinary report:

```powershell
py -3.14 test_demo.py
```

`test_demo.py` imports the application functions and runs assertions, ending with `Checks passed.` The application does not import or execute the tests. Do not use Python's `-O` flag for verification because it disables assertions; the test script rejects that mode.

## Code Landmarks

- `validate_record`: determine whether equipment details can be trusted.
- `color_text` and `print_color`: keep ANSI presentation separate from selection rules.
- `battery_meets_requirement`: express the inclusive battery rule.
- `exclusion_reason`: apply validation and loan rules, producing helpful explanations.
- `select_equipment`: return selected copies and excluded copies with explanations.
- `render_report` and `show_report`: present the useful answer.
- `initial_battery_rule`: clearly isolated teaching mistake, not application logic.
- `show_walkthrough`: connect the representations, comparisons, and corrected report.
- `main`: handle the small menu using familiar loops and decisions.
- `test_demo.py`: check expected selections, boundaries, invalid data, unchanged inventory, and report behavior separately.

Every function has a short docstring stating its purpose. Changing the display does not change who qualifies. Changing a request rule can change the answer even when the display remains identical.

[All daily demos](../../README.md)
