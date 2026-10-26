"""Small fictional campus-help-desk records for AL03."""

SUPPORTED_CATEGORIES = {"account", "network", "software", "classroom"}

TICKETS = [
    {
        "id": "T301",
        "title": "Cannot sign in to the student portal",
        "category": "account",
        "priority": "normal",
        "status": "open",
    },
    {
        "id": "T302",
        "title": "Library laptop cannot join campus Wi-Fi",
        "category": "network",
        "priority": "high",
        "status": "open",
    },
    {
        "id": "T303",
        "title": "Install the course code editor",
        "category": "software",
        "priority": "normal",
        "status": "open",
    },
    {
        "id": "T304",
        "title": "Update the recovery email address",
        "category": "account",
        "priority": "low",
        "status": "open",
    },
    {
        "id": "T305",
        "title": "Campus printer is not reachable",
        "category": "network",
        "priority": "normal",
        "status": "open",
    },
    {
        "id": "T306",
        "title": "Restore the missing spreadsheet shortcut",
        "category": "software",
        "priority": "low",
        "status": "completed",
    },
]
