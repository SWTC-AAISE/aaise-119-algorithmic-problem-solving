"""Supplied fictional campus connections, shared by this demo's examples."""

GRAPH = {
    "Library": ["Atrium", "Lab"],
    "Atrium": ["Library", "Cafe"],
    "Lab": ["Library", "Studio"],
    "Cafe": ["Atrium", "Studio"],
    "Studio": ["Lab", "Cafe"],
    "Annex": [],
}
