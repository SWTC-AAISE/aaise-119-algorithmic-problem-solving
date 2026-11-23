"""Real Python documentation references with locally assigned teaching tags.

Source identities/selected headings checked November 15, 2026 against official
Python 3.14 documentation. These URLs are sample data, not extra required reading.
Tags are retained local teaching metadata; they are not publisher classifications.
No resource contents or invented reading-time/difficulty estimates are included.
"""

PROFILE = {"queues", "stacks"}
WEIGHTS = {"queues": 4}
LIMIT = 2
LIMITATION_ID = "LR013"

# LR003 intentionally precedes LR002 so input order cannot settle their tie.
RESOURCES = [
    {
        "id": "LR001",
        "title": "More on Lists",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#more-on-lists",
        "tags": [
            "collections"
        ]
    },
    {
        "id": "LR003",
        "title": "Using Lists as Queues",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#using-lists-as-queues",
        "tags": [
            "queues",
            "collections"
        ]
    },
    {
        "id": "LR002",
        "title": "Using Lists as Stacks",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#using-lists-as-stacks",
        "tags": [
            "stacks",
            "collections"
        ]
    },
    {
        "id": "LR006",
        "title": "Tuples and Sequences",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#tuples-and-sequences",
        "tags": [
            "collections"
        ]
    },
    {
        "id": "LR007",
        "title": "Sets",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#sets",
        "tags": [
            "collections",
            "similarity"
        ]
    },
    {
        "id": "LR009",
        "title": "Looping Techniques",
        "url": "https://docs.python.org/3.14/tutorial/datastructures.html#looping-techniques",
        "tags": [
            "collections",
            "filtering"
        ]
    },
    {
        "id": "LR013",
        "title": "collections.deque",
        "url": "https://docs.python.org/3.14/library/collections.html#collections.deque",
        "tags": [
            "queues",
            "stacks",
            "collections"
        ]
    },
    {
        "id": "LR020",
        "title": "Modules",
        "url": "https://docs.python.org/3.14/tutorial/modules.html",
        "tags": [
            "modularity"
        ]
    }
]
