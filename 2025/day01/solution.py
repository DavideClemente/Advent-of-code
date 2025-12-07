"""
Advent of Code - Day 01
https://adventofcode.com/2025/day/1
"""

from common import read_input, read_lines
from pathlib import Path
import sys
import re

from common.dial import Dial, Rotation

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))

regex = re.compile(r"([LR])(\d+)")


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""

    dial = Dial(pointer=50)
    for instruction in data:
        matches = regex.findall(instruction)
        for (turn, steps) in matches:
            match turn:
                case "L":
                    dial.rotate(Rotation.LEFT, int(steps))
                case "R":
                    dial.rotate(Rotation.RIGHT, int(steps))
    return dial.zero_endings


def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    dial = Dial(pointer=50)
    for instruction in data:
        matches = regex.findall(instruction)
        for (turn, steps) in matches:
            match turn:
                case "L":
                    dial.rotate(Rotation.LEFT, int(steps))
                case "R":
                    dial.rotate(Rotation.RIGHT, int(steps))
    return dial.zero_endings + dial.zero_passes


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
