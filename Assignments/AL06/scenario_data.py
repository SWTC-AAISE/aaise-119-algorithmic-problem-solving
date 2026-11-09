"""Comparable fictional nested data; choose one application for AL06."""


def make_entry(name, amount, status):
    """Build a leaf record without performing eligibility or aggregation."""
    return {"type": "entry", "name": name, "amount": amount, "status": status}


def make_group(name, items):
    """Build a group record containing the supplied child records."""
    return {"type": "group", "name": name, "items": items}


SCENARIOS = {
    "fundraiser": {
        "title": "Fundraiser Tracker",
        "unit": "whole dollars",
        "included_status": "received",
        "data": make_group("Community fundraiser", [
            make_entry("Welcome-table donations", 25, "received"),
            make_group("North team", [
                make_entry("Bake-sale donations", 40, "received"),
                make_entry("Sponsor promise", 90, "pledged"),
                make_group("Student volunteers", [
                    make_entry("Collection jar", 15, "received"),
                    make_entry("Matching pledge", 35, "pledged"),
                ]),
            ]),
            make_entry("Online promise", 10, "pledged"),
            make_group("New team", []),
        ]),
    },
    "project": {
        "title": "Project Effort Estimator",
        "unit": "hours",
        "included_status": "unfinished",
        "data": make_group("Community website project", [
            make_entry("Review page content", 6, "unfinished"),
            make_group("Member features", [
                make_entry("Build signup page", 4, "unfinished"),
                make_entry("Draft navigation", 8, "finished"),
                make_group("Accessibility", [
                    make_entry("Check keyboard access", 3, "unfinished"),
                    make_entry("Choose heading structure", 2, "finished"),
                ]),
            ]),
            make_entry("Choose project name", 5, "finished"),
            make_group("Future work", []),
        ]),
    },
    "inventory": {
        "title": "Inventory Counter",
        "unit": "items",
        "included_status": "usable",
        "data": make_group("Community activity supplies", [
            make_entry("Front-desk markers", 12, "usable"),
            make_group("Activity room", [
                make_entry("Paper packs", 8, "usable"),
                make_entry("Torn folders", 7, "damaged"),
                make_group("Supply cabinet", [
                    make_entry("Working scissors", 5, "usable"),
                    make_entry("Broken rulers", 4, "damaged"),
                ]),
            ]),
            make_entry("Dried glue sticks", 2, "damaged"),
            make_group("New storage bin", []),
        ]),
    },
}
