"""Supplied small cases for the minimum-coin investigation."""

CASES = [
    {"label": "A shorter exact payment exists", "coins": [1, 4, 6], "target": 8},
    {"label": "Largest-first gets stuck", "coins": [4, 6], "target": 8},
    {"label": "No exact payment exists", "coins": [4, 6], "target": 7},
    {"label": "Both methods agree", "coins": [1, 5, 10], "target": 12},
]
