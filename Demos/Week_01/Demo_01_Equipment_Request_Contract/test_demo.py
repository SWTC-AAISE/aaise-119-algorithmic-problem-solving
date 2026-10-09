"""Verify selection, the intentional teaching failure, presentation, and the menu."""

import ast
import os
import re
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import main as demo
import console_style


def capture_output(action, *args, **kwargs):
    """Run an action and return its console output for comparison."""
    output = StringIO()
    with redirect_stdout(output):
        action(*args, **kwargs)
    return output.getvalue()


def check_selection():
    """Verify loan rules, invalid data, boundary values, and independent copies."""
    selected, excluded = demo.select_equipment(demo.EQUIPMENT, "laptop")
    assert [row["id"] for row in selected] == ["E01", "E04"]
    assert [row["id"] for row, _ in excluded] == ["E02", "E03", "E05"]
    assert demo.select_equipment([], "laptop") == ([], [])
    assert demo.select_equipment(demo.EQUIPMENT, "camera")[0] == []
    assert demo.validate_record({"id": "X", "type": "laptop", "available": 1, "battery": True})
    for battery in (0, 100):
        record = {"id": "X", "type": "laptop", "available": True, "battery": battery}
        assert not demo.validate_record(record)
    for battery in (True, -1, 101, "50", None):
        record = {"id": "X", "type": "laptop", "available": True, "battery": battery}
        matches, exclusions = demo.select_equipment([record], "laptop")
        assert matches == [] and len(exclusions) == 1
        assert "checking" in exclusions[0][1] or "check before lending" in exclusions[0][1]
    for record in ({"available": True, "battery": None},
                   {"id": " ", "type": "laptop", "available": True, "battery": 80}):
        assert demo.select_equipment([record], "laptop")[0] == []
    selected[0]["battery"] = 0
    excluded[0][0]["available"] = True
    assert demo.EQUIPMENT[0]["battery"] == 80
    assert demo.EQUIPMENT[1]["available"] is False
    for threshold in (-1, 101, True, "50"):
        try:
            demo.select_equipment(demo.EQUIPMENT, "laptop", threshold)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid battery requirement was accepted")


def check_report():
    """Verify readable results without traces, test banners, or raw Python lists."""
    for threshold, expected in ((50, "Result: 2 laptops meet"),
                                (80, "Result: 1 laptop meets"),
                                (100, "No laptops meet this request.")):
        output = capture_output(demo.show_report, threshold)
        assert expected in output
        for unwanted in ("trace", "Checks passed.", "invalid:", "['E01'"):
            assert unwanted not in output
    report = capture_output(demo.show_report)
    assert "E04 - Laptop - Battery 50%" in report
    assert "E05 - Battery not recorded; check before lending" in report
    assert "Not included" not in demo.render_report([], [], 50)
    assert "No laptops meet this request." in demo.render_report([], [], 50)
    readme = Path(demo.__file__).with_name("README.md").read_text()
    expected_report = readme.split("```text\n", 1)[1].split("```", 1)[0]
    assert report == expected_report


def check_walkthrough():
    """Ensure the teaching mistake fails once and the real selection passes."""
    cases = demo.walkthrough_cases()
    assert [demo.initial_battery_rule(row["battery"], 50) == expected
            for _, row, expected in cases[:3]] == [True, False, True]
    for _, record, expected in cases:
        assert bool(demo.select_equipment([record], "laptop")[0]) == expected
    initial = capture_output(demo.show_comparisons, cases[:3], use_initial_rule=True)
    revised = capture_output(demo.show_comparisons, cases)
    assert len([line for line in initial.splitlines() if line.endswith("No")]) == 1
    assert all(line.endswith("Yes") for line in revised.splitlines()[2:])
    output = capture_output(demo.show_walkthrough, pause=False)
    landmarks = ("1. Before Revision", "2. After Revision", "3. Representation Bridge",
                 "4. Initial Rule", "5. Revised Rule", "6. The Useful Answer")
    positions = [output.index(label) for label in landmarks]
    assert positions == sorted(positions)
    assert "Pseudocode" in output and "return battery >= minimum_battery" in output
    assert output.endswith(capture_output(demo.show_report))
    assert "Checks passed." not in output
    assert max(map(len, output.splitlines())) <= 80
    with patch("builtins.input", side_effect=[""] * 5):
        paused_output = capture_output(demo.show_walkthrough)
    assert paused_output == output
    with patch("builtins.input", side_effect=EOFError):
        stopped = capture_output(demo.show_walkthrough)
    assert "Walkthrough stopped." in stopped and "6. The Useful Answer" not in stopped


def check_menu():
    """Exercise both menu options, invalid choices, repeated use, and clean exits."""
    with patch("builtins.input", side_effect=["bad", "1", "2", *([""] * 5), "1", "0"]):
        output = capture_output(demo.main)
    assert "Please choose 1, 2, or 0." in output
    assert output.count("Result: 2 laptops meet the request.") == 3
    assert "Representation Bridge" in output and output.endswith("Goodbye.\n")
    for interruption in (EOFError, KeyboardInterrupt):
        with patch("builtins.input", side_effect=interruption):
            assert capture_output(demo.main).endswith("Goodbye.\n")


def check_colors():
    """Verify semantic colors, resets, unchanged text, and plain-output fallbacks."""
    ansi_pattern = re.compile(r"\x1b\[[0-9;]*m")
    for action in (demo.show_report, lambda: demo.show_walkthrough(pause=False)):
        plain = capture_output(action)
        output = StringIO()
        with patch.dict(os.environ, {"TERM": "xterm"}, clear=True):
            with redirect_stdout(output), patch.object(output, "isatty", return_value=True):
                action()
        colored = output.getvalue()
        assert "\033[96m" in colored and "\033[92m" in colored
        assert ansi_pattern.sub("", colored) == plain
        assert colored.count(console_style.RESET) == sum(colored.count(code) for code in console_style.COLORS.values())
        if action is demo.show_report:
            assert "\033[93mNot included\033[0m" in colored
        else:
            assert "\033[91mNo\033[0m" in colored
            assert "\033[92mYes\033[0m" in colored
            assert "\033[0;37;44m" in colored
            assert "\033[0;37;44m      return battery >= minimum_battery\033[0m" in colored
            assert "\033[94m" not in colored
    for environment in ({"NO_COLOR": ""}, {"NO_COLOR": "1"}, {"TERM": "dumb"}):
        output = StringIO()
        with patch.dict(os.environ, environment, clear=True):
            with redirect_stdout(output), patch.object(output, "isatty", return_value=True):
                demo.show_walkthrough(pause=False)
        assert "\033[" not in output.getvalue()
    assert "\033[" not in capture_output(demo.show_walkthrough, pause=False)


def self_check():
    """Run all regression groups and enforce short function-purpose docstrings."""
    check_selection()
    check_report()
    check_walkthrough()
    check_menu()
    check_colors()
    for path in (Path(demo.__file__), Path(__file__)):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                assert docstring and len(docstring.splitlines()) == 1, node.name
        if path.name == "main.py":
            assert not any(isinstance(node, ast.Assert) for node in ast.walk(tree))
            assert "argparse" not in path.read_text() and "trace" not in path.read_text().lower()


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
