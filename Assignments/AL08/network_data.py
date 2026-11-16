"""Supplied fictional workshop model and individual blocked-node cases."""

GRAPH = {
    "Entrance": ["Reception"],
    "Reception": ["Entrance", "Hallway", "Office"],
    "Hallway": ["Reception", "ToolRoom", "Assembly", "BreakRoom"],
    "ToolRoom": ["Hallway", "Assembly"],
    "Assembly": ["Hallway", "ToolRoom", "Inspection"],
    "Inspection": ["Assembly", "Packing", "Training"],
    "Packing": ["Inspection", "Loading"],
    "Loading": ["Packing", "Office"],
    "Office": ["Reception", "Loading"],
    "BreakRoom": ["Hallway", "Training"],
    "Training": ["BreakRoom", "Inspection"],
    "Annex": [],
}
START = "Entrance"
GOAL = "Loading"
RESTRICTIONS = {
    "A": {"label": "Office unavailable", "blocked": ["Office"]},
    "B": {"label": "Office and Packing unavailable", "blocked": ["Office", "Packing"]},
    "C": {"label": "Packing unavailable", "blocked": ["Packing"]},
}
