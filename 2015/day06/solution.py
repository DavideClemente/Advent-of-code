"""
Advent of Code - Day 06
https://adventofcode.com/2015/day/6
"""

from common import read_input, read_lines
from pathlib import Path
from common.grid import Matrix
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    matrix = Matrix.create_empty(1000, 1000, -1)
    for line in data:
        instruction = line.split()[0]
        if instruction == "toggle":
            x1, y1, x2, y2 = map(int, line.split()[1].split(
                ",") + line.split()[3].split(","))
            matrix.apply_to_interval(x1, y1, x2 + 1, y2 + 1, lambda x: x * -1)
        else:
            on_off = line.split()[1]
            x1, y1, x2, y2 = map(int, line.split()[2].split(
                ",") + line.split()[4].split(","))
            matrix.apply_to_interval(x1, y1, x2 + 1, y2 + 1, lambda x: 1 if on_off == "on" else -1)
    return matrix.count_matching(lambda x: x == 1)


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    matrix = Matrix.create_empty(1000, 1000, 0)
    for line in data:
        instruction = line.split()[0]
        if instruction == "toggle":
            x1, y1, x2, y2 = map(int, line.split()[1].split(
                ",") + line.split()[3].split(","))
            matrix.apply_to_interval(x1, y1, x2 + 1, y2 + 1, lambda x: x + 2)
        else:
            on_off = line.split()[1]
            x1, y1, x2, y2 = map(int, line.split()[2].split(
                ",") + line.split()[4].split(","))
            matrix.apply_to_interval(x1, y1, x2 + 1, y2 + 1, lambda x: x + 1 if on_off == "on" else max(0, x - 1))
    return sum(sum(row) for row in matrix.data)


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
