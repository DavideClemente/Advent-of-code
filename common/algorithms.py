"""Common algorithms for graph traversal and pathfinding."""

from collections import deque
from heapq import heappush, heappop
from typing import Callable, Dict, List, Set, Tuple, TypeVar, Optional, Hashable

T = TypeVar('T', bound=Hashable)


def bfs(
    start: T,
    neighbors_fn: Callable[[T], List[T]],
    goal_fn: Optional[Callable[[T], bool]] = None
) -> Dict[T, int]:
    """
    Breadth-first search.

    Args:
        start: Starting node
        neighbors_fn: Function that returns neighbors of a node
        goal_fn: Optional function to check if we've reached the goal

    Returns:
        Dictionary mapping nodes to their distance from start
    """
    queue = deque([start])
    distances = {start: 0}

    while queue:
        current = queue.popleft()

        if goal_fn and goal_fn(current):
            return distances

        for neighbor in neighbors_fn(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def dfs(
    start: T,
    neighbors_fn: Callable[[T], List[T]],
    goal_fn: Optional[Callable[[T], bool]] = None
) -> Set[T]:
    """
    Depth-first search.

    Args:
        start: Starting node
        neighbors_fn: Function that returns neighbors of a node
        goal_fn: Optional function to check if we've reached the goal

    Returns:
        Set of all visited nodes
    """
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if goal_fn and goal_fn(current):
            return visited

        for neighbor in neighbors_fn(current):
            if neighbor not in visited:
                stack.append(neighbor)

    return visited


def dijkstra(
    start: T,
    neighbors_fn: Callable[[T], List[Tuple[T, int]]],
    goal_fn: Optional[Callable[[T], bool]] = None
) -> Dict[T, int]:
    """
    Dijkstra's shortest path algorithm.

    Args:
        start: Starting node
        neighbors_fn: Function that returns (neighbor, cost) tuples
        goal_fn: Optional function to check if we've reached the goal

    Returns:
        Dictionary mapping nodes to their shortest distance from start
    """
    heap = [(0, start)]
    distances = {start: 0}

    while heap:
        current_dist, current = heappop(heap)

        if goal_fn and goal_fn(current):
            return distances

        if current_dist > distances.get(current, float('inf')):
            continue

        for neighbor, cost in neighbors_fn(current):
            new_dist = current_dist + cost

            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heappush(heap, (new_dist, neighbor))

    return distances


def a_star(
    start: T,
    goal: T,
    neighbors_fn: Callable[[T], List[Tuple[T, int]]],
    heuristic_fn: Callable[[T, T], int]
) -> Tuple[Optional[List[T]], int]:
    """
    A* pathfinding algorithm.

    Args:
        start: Starting node
        goal: Goal node
        neighbors_fn: Function that returns (neighbor, cost) tuples
        heuristic_fn: Heuristic function estimating cost from node to goal

    Returns:
        Tuple of (path from start to goal, total cost), or (None, inf) if no path
    """
    heap = [(0, start)]
    g_scores = {start: 0}
    f_scores = {start: heuristic_fn(start, goal)}
    came_from = {}

    while heap:
        _, current = heappop(heap)

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path)), g_scores[goal]

        for neighbor, cost in neighbors_fn(current):
            tentative_g = g_scores[current] + cost

            if tentative_g < g_scores.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                f_scores[neighbor] = tentative_g + heuristic_fn(neighbor, goal)
                heappush(heap, (f_scores[neighbor], neighbor))

    return None, float('inf')
