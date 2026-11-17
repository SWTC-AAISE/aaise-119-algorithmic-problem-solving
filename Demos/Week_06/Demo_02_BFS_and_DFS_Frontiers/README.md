# BFS and DFS Frontiers

DEM-W06D02 | Week 6, Tuesday

Find reachable buildings, then compare the queue/stack choices used to inspect them.

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

BFS uses a queue and marks a building discovered when enqueued.
Iterative DFS uses a stack and marks a building visited when popped for processing;
entries already processed are skipped. Both process the reachable component only.
Fixed neighbor order makes these examples repeatable without defining one universal
DFS order. Discovery/processed membership is different from pending order.

## Code Landmarks

- breadth_first: explicit FIFO implementation.
- depth_first: explicit LIFO implementation.
- traverse: compatibility wrapper for the earlier interface, not the first teaching entry point.
- main2.py: annotated equivalent of main.py.
- graph_support.py: supplied reference checks and independent teaching snapshots.
- graph_display.py, graph_data.py, console_style.py: supplied presentation/data.

## Reading the Teaching Table

Queue front is left; stack top is right. Snapshot rows follow processing of a
new building. BFS's Discovered column includes waiting buildings; DFS's Processed
so far column includes completed visits. Those membership labels are alphabetical,
not discovery order. DFS can have duplicate pending entries and skips ones already
processed; keep that guard brief rather than turning anomalies into another topic.

Two compact tables follow the unchanged Teaching views: one for the BFS queue
(front to rear), then one for the DFS stack (bottom to top). Step 0 shows the
initial structure; subsequent rows show its actual contents after processing the
named building and adding its eligible neighbors. `[]` means empty. Duplicate
DFS entries remain visible; the last visit can leave an already-processed entry
that is later skipped.

Core adjacency traversal has introductory O(V + E) work; copied frontier snapshots
and sorted labels add teaching overhead. Ten adjacency entries represent five
undirected connections here. No benchmark or timing exercise is required.

## Expected Default Run

```text
CAMPUS CONNECTION EXPLORER
Which buildings can we reach from Library?

Reachable buildings: Library, Atrium, Lab, Cafe, Studio
Not reachable from this start: Annex

BFS visit order: Library, Atrium, Lab, Cafe, Studio
DFS visit order: Library, Atrium, Cafe, Studio, Lab
Visit order describes inspection, not a walking route.

Teaching view - BFS: queue front is on the left
Step  Processed  Pending (stored order)         Discovered (alphabetical)
1     Library    Atrium, Lab                    Atrium, Lab, Library
2     Atrium     Lab, Cafe                      Atrium, Cafe, Lab, Library
3     Lab        Cafe, Studio                   Atrium, Cafe, Lab, Library, Studio
4     Cafe       Studio                         Atrium, Cafe, Lab, Library, Studio
5     Studio     (empty)                        Atrium, Cafe, Lab, Library, Studio

Teaching view - DFS: stack top is on the right
Step  Processed  Pending (stored order)         Processed so far (alphabetical)
1     Library    Lab, Atrium                    Library
2     Atrium     Lab, Cafe                      Atrium, Library
3     Cafe       Lab, Studio                    Atrium, Cafe, Library
4     Studio     Lab, Lab                       Atrium, Cafe, Library, Studio
5     Lab        Lab                            Atrium, Cafe, Lab, Library, Studio
Rows show new visits; DFS skips any remaining already-processed entries.

BFS queue: FRONT -> REAR
Removes the front item, then adds newly discovered neighbors at the rear.
Step  Processed  Contents
0     (start)    [Library]
1     Library    [Atrium, Lab]
2     Atrium     [Lab, Cafe]
3     Lab        [Cafe, Studio]
4     Cafe       [Studio]
5     Studio     []

DFS stack: BOTTOM -> TOP
Removes the top item, then pushes eligible neighbors onto the top.
Step  Processed  Contents
0     (start)    [Library]
1     Library    [Lab, Atrium]
2     Atrium     [Lab, Cafe]
3     Cafe       [Lab, Studio]
4     Studio     [Lab, Lab]
5     Lab        [Lab]

Adjacency entries examined: BFS 10; DFS 10.
Each of the five undirected connections has two adjacency entries.
Core traversal work is O(V + E); teaching snapshots and sorting add work.
```

## Explore

Why does BFS inspect outward layers while DFS follows the most recent pending branch?
Why is the complete visit list not necessarily a walking route?

[All daily demos](../../README.md)
