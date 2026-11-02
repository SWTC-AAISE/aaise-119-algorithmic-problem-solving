"""Reusable console colors, separate from application rules."""

import os
import sys

COLORS = {
    "heading": "\033[96m",
    "success": "\033[92m",
    "caution": "\033[93m",
    "failure": "\033[91m",
    "code": "\033[0;37;44m",
}
RESET = "\033[0m"


def color_text(text, color):
    """Color terminal text unless output or environment requires plain text."""
    if not sys.stdout.isatty() or "NO_COLOR" in os.environ or os.environ.get("TERM") == "dumb":
        return text
    return f"{COLORS[color]}{text}{RESET}"


def print_color(text, color):
    """Print a line using the reusable console palette."""
    print(color_text(text, color))
