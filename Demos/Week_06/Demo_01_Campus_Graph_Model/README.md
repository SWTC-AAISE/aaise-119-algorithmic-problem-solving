# Campus Graph Model

DEM-W06D01 | Week 6, Monday

Check the direct connections in a small fictional map before relying on it.

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

The model is an undirected adjacency list with explicit reciprocal entries.
A building may exist without connections: Annex is valid disconnected data.
The checker reports duplicate, unknown, and missing reciprocal references;
it does not validate every possible graph property or real-world condition.

## Code Landmarks

- main.py: readable validate_graph plus the small example driver.
- main2.py: the same behavior with detailed explanations and an optional compact-copy comparison.
- graph_data.py: the six-building fixture.
- graph_display.py and console_style.py: supplied readable presentation.

## Expected Default Run

```text
CAMPUS MAP CHECK
Check direct walking connections before using this fictional map.

Direct walking connections
  Library: Atrium, Lab
  Atrium: Library, Cafe
  Lab: Library, Studio
  Cafe: Atrium, Studio
  Studio: Lab, Cafe
  Annex: No direct connections in this model

Original map
  Connection checks passed.

Map with a deliberately mistyped connection
  Please correct these connections:
  - Library: unknown node Gym

A cycle: Library - Atrium - Cafe - Studio - Lab - Library
Annex exists in the model but has no direct connections.
Connections work both ways; distance, hours and accessibility are not modeled.
```

## Explore

Why is an unknown Gym reference a mistake, while Annex is valid?
Which real-world details would you need before using this as a real walking map?

[All daily demos](../../README.md)
