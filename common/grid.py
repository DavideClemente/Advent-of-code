"""Common grid and point utilities for 2D grid problems."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Set, Optional, Iterator


@dataclass(frozen=True)
class Point:
    """Represents a point in 2D space."""
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)

    def manhattan_distance(self, other: 'Point') -> int:
        """Calculate Manhattan distance to another point."""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def neighbors(self, diagonal: bool = False) -> List['Point']:
        """Get adjacent points (4 or 8 directions)."""
        points = [
            Point(self.x + 1, self.y),
            Point(self.x - 1, self.y),
            Point(self.x, self.y + 1),
            Point(self.x, self.y - 1),
        ]
        if diagonal:
            points.extend([
                Point(self.x + 1, self.y + 1),
                Point(self.x + 1, self.y - 1),
                Point(self.x - 1, self.y + 1),
                Point(self.x - 1, self.y - 1),
            ])
        return points


class Direction(Enum):
    """Cardinal directions."""
    NORTH = Point(0, -1)
    SOUTH = Point(0, 1)
    EAST = Point(1, 0)
    WEST = Point(-1, 0)

    def turn_right(self) -> 'Direction':
        """Turn 90 degrees clockwise."""
        turns = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        return turns[self]

    def turn_left(self) -> 'Direction':
        """Turn 90 degrees counter-clockwise."""
        turns = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }
        return turns[self]

    def reverse(self) -> 'Direction':
        """Get opposite direction."""
        reverses = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return reverses[self]


class Grid:
    """2D grid with common operations."""

    def __init__(self, data: List[List[str]]):
        """
        Initialize grid from 2D list.

        Args:
            data: 2D list representing the grid
        """
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if data else 0

    def get(self, point: Point, default: Optional[str] = None) -> Optional[str]:
        """Get value at point, return default if out of bounds."""
        if self.in_bounds(point):
            return self.data[point.y][point.x]
        return default

    def set(self, point: Point, value: str) -> None:
        """Set value at point."""
        if self.in_bounds(point):
            self.data[point.y][point.x] = value

    def in_bounds(self, point: Point) -> bool:
        """Check if point is within grid bounds."""
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def find(self, value: str) -> Optional[Point]:
        """Find first occurrence of value in grid."""
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell == value:
                    return Point(x, y)
        return None

    def find_all(self, value: str) -> List[Point]:
        """Find all occurrences of value in grid."""
        points = []
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell == value:
                    points.append(Point(x, y))
        return points

    def neighbors(self, point: Point, diagonal: bool = False) -> Iterator[Point]:
        """Get valid neighboring points."""
        for neighbor in point.neighbors(diagonal):
            if self.in_bounds(neighbor):
                yield neighbor

    def __str__(self) -> str:
        """String representation of the grid."""
        return '\n'.join(''.join(row) for row in self.data)

    def copy(self) -> 'Grid':
        """Create a deep copy of the grid."""
        return Grid([row[:] for row in self.data])
