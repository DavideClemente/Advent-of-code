"""
Advent of Code - Day 09
https://adventofcode.com/2025/day/9
"""

from common import read_input, read_lines, Point
from pathlib import Path
from dataclasses import dataclass, field
from py_linq.py_linq import Enumerable
from itertools import combinations
import sys


@dataclass
class Rectangle():
    cornerA: Point
    cornerB: Point
    area: float = field(init=False)

    def __post_init__(self):
        """Called automatically after __init__"""
        self.area = self.rectangle_area()

    def rectangle_area(self) -> float:
        if self.cornerA.x == self.cornerB.x:
            return abs(self.cornerA.y - self.cornerB.y)
        elif self.cornerA.y == self.cornerB.y:
            return abs(self.cornerA.x - self.cornerB.x)
        else:
            width = abs(self.cornerA.x - self.cornerB.x) + 1
            height = abs(self.cornerA.y - self.cornerB.y) + 1
            return width * height


# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    points = Enumerable(data).select(
        lambda x: Point(*map(int, x.split(',')))).to_list()
    rectangles = list(combinations(points, 2))
    biggest_rectangle = Enumerable(rectangles).select(lambda x: Rectangle(
        x[0], x[1])).order_by_descending(lambda x: x.area).first().area
    return biggest_rectangle


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    pass


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
