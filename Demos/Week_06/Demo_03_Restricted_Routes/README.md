# Restricted Routes

DEM-W06D03 | Week 6, Thursday

Find a fewest-hop route while avoiding selected buildings.

## Run

From this folder:

```powershell
py -3.14 main.py
py -3.14 main2.py
py -3.14 test_demo.py
```

Use python if it selects the course interpreter. Python 3.14 standard library only;
no third-party packages, network, web framework, or sibling-demo imports.
Keep all supplied local .py modules together. The program does not write files.
Tests are separate and must run without -O. Colors use the established shared
palette and become plain text when output is redirected or NO_COLOR is set.

## Contract

BFS minimizes the number of connections on this unweighted model.
shortest_hop_path returns (path, parents), with None for a valid but unavailable
route or a blocked endpoint. Unknown requested buildings and neighbor references
raise a clear ValueError through supplied quality checks. start=goal returns a
one-building path with zero hops unless the endpoint is blocked.

This demo blocks nodes only. Illustrative distances use fictional units and do
not introduce a weighted shortest-path implementation.

## Code Landmarks

- shortest_hop_path: queue-based search with a parent entry for each discovered building.
- reconstruct_path: goal-to-start links reversed into the user's route order.
- main2.py: annotated equivalent of main.py.
- route_support.py: supplied parser, quality checks, and an explicit distance-summing loop.
- graph_support.py: supplied reference validation.
- graph_data.py, graph_display.py, console_style.py: supplied model and presentation.

## Supplied --blocked Input

| Command | Meaning |
| --- | --- |
| py -3.14 main.py | Default: avoid Lab. |
| py -3.14 main.py --blocked | Apply no restrictions. |
| py -3.14 main.py --blocked Lab Cafe | Avoid both buildings; no route remains in this example. |
| py -3.14 main.py --help | Show the supplied interface. |

The option extends Week 5's argparse introduction: nargs="*" reads zero or more
names into a list, while choices limits names to this fixture. Parser construction
is supplied support, not a new assessed implementation requirement.

## Expected Default Run

```text
CAMPUS ROUTE FINDER
Find a route from Library to Studio with the fewest walking connections.

With all buildings available
Route: Library -> Lab -> Studio
Walking connections: 2
Illustrative distance: 16 units

Buildings to avoid
Lab

With the selected restrictions
Route: Library -> Atrium -> Cafe -> Studio
Walking connections: 3
Illustrative distance: 3 units

Fewest hops does not guarantee the shortest distance or travel time.
Distances are supplied illustrative units; BFS does not optimize them.

Teaching view - how BFS first reached each building
  Library: start building
  Atrium: first reached from Library
  Lab: first reached from Library
  Cafe: first reached from Atrium
  Studio: first reached from Lab

Library to disconnected Annex
No permitted route is available.

Already at Library
Route: Library
Walking connections: 0
Illustrative distance: 0 units
```

## Explore

Why can the two-hop route have more distance units than the three-hop route?
How does a saved parent help us reconstruct a route?

[All daily demos](../../README.md)
