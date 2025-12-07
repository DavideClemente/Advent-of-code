"""
Advent of Code - Day XX
https://adventofcode.com/YYYY/day/XX
"""

from common import read_input, read_lines
from pathlib import Path
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    # TODO: Implement solution
    pass


def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    pass


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_input(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
