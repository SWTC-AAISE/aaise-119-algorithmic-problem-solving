"""Optional AL08 starter: model Monday, traversals Tuesday, routes Thursday."""

from collections import deque
from network_support import validate_request, record_step
from app_runner import run

STAGE = 1  # Monday 1; Tuesday 2 when traversals work; Thursday 3 when routes work.
MY_RESTRICTION = "A"  # Set this to your instructor-issued case in your personal copy.


# MONDAY — Inspect the supplied model and test copies with a connection mistake.
# No traversal is required for STAGE 1; keep your brief personal model notes.


# TUESDAY — Complete each algorithm separately on the fresh common fixture.
def breadth_first(graph, start):
    """Return BFS order, independent snapshots, and adjacency entries examined."""
    validate_request(graph, start)
    # Begin a deque with start and a discovered set containing start.
    # Use separate order, trace, and edge-count state.
    # Process the queue from the left and append each new visit to order.
    # Examine neighbors in their listed order, counting each adjacency entry.
    # Mark an undiscovered neighbor before adding it to the queue.
    # Use record_step(trace, node, queue, discovered) after neighbor handling.
    # Return order, trace, and the count; leave graph unchanged.
    raise NotImplementedError("Complete breadth-first traversal.")


def depth_first(graph, start):
    """Return iterative DFS order, independent snapshots, and adjacency count."""
    validate_request(graph, start)
    # Begin a list stack with start and an empty visited set.
    # Pop from the right; skip an entry already processed.
    # Mark this new visit and record its order.
    # Consider reversed neighbors so the first listed neighbor is taken next.
    # Count each adjacency entry and push neighbors not yet visited.
    # Use record_step(trace, node, stack, visited) after neighbor handling.
    # Return order, trace, and the count; leave graph unchanged.
    raise NotImplementedError("Complete iterative depth-first traversal.")


# THURSDAY — Save parents during BFS, then follow one chain backward.
def reconstruct_path(parents, goal):
    """Return start-to-goal order by following the BFS parent chain."""
    # Begin at goal and collect names until the parent is None.
    # Reverse the new list before returning it; preserve parents.
    raise NotImplementedError("Complete parent-chain reconstruction.")


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted fewest-hop path and parents, or None with parent state."""
    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)
    # A blocked start or goal returns None and an empty dictionary.
    # Begin parents with start: None and a queue containing start.
    # Process the queue; on reaching goal, return the reconstructed path and parents.
    # For a neighbor not in parents and not blocked, save its first parent and enqueue.
    # If the queue runs out, return None and the parents collected.
    raise NotImplementedError("Complete BFS with parents and blocked nodes.")


def main():
    """Run only the selected completed stage using supplied presentation."""
    run(STAGE, breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION)


if __name__ == "__main__":
    main()
