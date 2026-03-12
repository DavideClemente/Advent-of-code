"""Common grid and point utilities for 2D grid problems."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Tuple, Set, Optional, Iterator


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


class Matrix:
    """2D matrix with numeric values and function application capabilities."""

    def __init__(self, data: List[List[int]]):
        """
        Initialize matrix from 2D list.

        Args:
            data: 2D list of numeric values representing the matrix
        """
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if data else 0

    @classmethod
    def create_empty(cls, rows: int, cols: int, default_value: int = 0) -> 'Matrix':
        """Create a matrix filled with a default value.

        Args:
            rows: Number of rows
            cols: Number of columns
            default_value: Value to fill all cells with (default: 0)

        Returns:
            A new Matrix instance

        Example:
            matrix = Matrix.create_empty(5, 5)        # Create 5x5 matrix filled with 0s
            matrix = Matrix.create_empty(3, 3, -1)    # Create 3x3 matrix filled with -1s
        """
        data = [[default_value for _ in range(cols)] for _ in range(rows)]
        return cls(data)

    def get(self, row: int, col: int, default: Optional[int] = None) -> Optional[int]:
        """Get value at [row, col], return default if out of bounds."""
        if self.in_bounds(row, col):
            return self.data[row][col]
        return default

    def set(self, row: int, col: int, value: int) -> None:
        """Set value at [row, col]."""
        if self.in_bounds(row, col):
            self.data[row][col] = value

    def in_bounds(self, row: int, col: int) -> bool:
        """Check if position is within matrix bounds."""
        return 0 <= row < self.height and 0 <= col < self.width

    def apply_to_cell(self, row: int, col: int, func) -> None:
        """Apply a function to a single cell, replacing its value with the result.

        Args:
            row: Row index
            col: Column index
            func: Function that takes a value and returns a new value

        Example:
            matrix.apply_to_cell(0, 0, lambda x: x * -1)  # Multiply by -1
            matrix.apply_to_cell(1, 2, lambda x: x + 1)   # Add 1
        """
        if self.in_bounds(row, col):
            self.data[row][col] = func(self.data[row][col])

    def apply_to_all(self, func) -> None:
        """Apply a function to all cells in the matrix.

        Args:
            func: Function that takes a value and returns a new value

        Example:
            matrix.apply_to_all(lambda x: x * 2)          # Double all values
            matrix.apply_to_all(lambda x: abs(x))         # Take absolute value
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = func(self.data[row][col])

    def apply_to_interval(self, row_start: int, col_start: int, row_end: int, col_end: int, func) -> None:
        """Apply a function to a rectangular interval of cells in the matrix.

        Args:
            row_start: Starting row index (inclusive)
            row_end: Ending row index (exclusive)
            col_start: Starting column index (inclusive)
            col_end: Ending column index (exclusive)
            func: Function that takes a value and returns a new value

        Example:
            matrix.apply_to_interval(0, 0, 2, 2, lambda x: x * -1)  # Multiply top-left 2x2 block by -1
            matrix.apply_to_interval(1, 1, 3, 3, lambda x: x + 1)   # Add 1 to bottom-right 2x2 block
        """
        for row in range(row_start, min(row_end, self.height)):
            for col in range(col_start, min(col_end, self.width)):
                self.data[row][col] = func(self.data[row][col])

    def count_matching(self, validation_func) -> int:
        """Count the number of cells that pass a validation function.

        Args:
            validation_func: Function that takes a value and returns True/False

        Returns:
            Number of cells where validation_func returns True

        Example:
            count = matrix.count_matching(lambda x: x > 0)         # Count positive values
            count = matrix.count_matching(lambda x: x == 5)        # Count cells equal to 5
            count = matrix.count_matching(lambda x: x % 2 == 0)    # Count even values
        """
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if validation_func(self.data[row][col]):
                    count += 1
        return count

    def row(self, index: int) -> List[int]:
        """Get a row from the matrix."""
        if 0 <= index < self.height:
            return self.data[index][:]
        return []

    def column(self, index: int) -> List[int]:
        """Get a column from the matrix."""
        if 0 <= index < self.width:
            return [self.data[row][index] for row in range(self.height)]
        return []

    def __str__(self) -> str:
        """String representation of the matrix."""
        return '\n'.join(' '.join(str(val) for val in row) for row in self.data)

    def copy(self) -> 'Matrix':
        """Create a deep copy of the matrix."""
        return Matrix([row[:] for row in self.data])
