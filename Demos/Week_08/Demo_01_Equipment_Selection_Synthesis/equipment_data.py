"""Small fictional loan inventory with valid fields and unique equipment IDs."""

EQUIPMENT = [
    {
        "id": "E01",
        "name": "Cedar laptop",
        "type": "laptop",
        "available": True,
        "battery": 80,
    },
    {
        "id": "E02",
        "name": "Maple laptop",
        "type": "laptop",
        "available": False,
        "battery": 90,
    },
    {
        "id": "E03",
        "name": "Studio tablet",
        "type": "tablet",
        "available": True,
        "battery": 95,
    },
    {
        "id": "E04",
        "name": "Birch laptop",
        "type": "laptop",
        "available": True,
        "battery": 50,
    },
]

REQUESTS = ["E01", "E02", "E03", "E04", "E99"]
