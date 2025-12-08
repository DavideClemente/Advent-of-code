"""
Advent of Code - Day 02
https://adventofcode.com/2025/day/2
"""

from common import read_input, read_lines
from pathlib import Path
import sys
import re

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))


def repeats_once(num: str) -> bool:
    """Check if string is exactly a pattern repeated twice (like 55, 6464, 123123)."""
    # Check if the string length is even
    if len(num) % 2 != 0:
        return False
    # Split in half and check if both halves are identical
    mid = len(num) // 2
    return num[:mid] == num[mid:]


def repeats_more_than_twice(num: str) -> bool:
    """Check if string is a pattern repeated more than twice (like 555, 646464, 123123123)."""
    length = len(num)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            pattern = num[:size]
            if pattern * (length // size) == num and (length // size) >= 2:
                return True
    return False


def count_invalids(start: int, end: int) -> int:
    invalids = 0
    for num in range(start, end+1):
        invalid = repeats_once(str(num))
        if invalid:
            invalids += num
    return invalids


def count_invalids_more_than_twice(start: int, end: int) -> int:
    invalids = 0
    for num in range(start, end+1):
        invalid = repeats_more_than_twice(str(num))
        if invalid:
            invalids += num
    return invalids


def part1(data: str) -> int:
    invalids = 0
    ranges = data.split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        invalids += count_invalids(start, end)
    return invalids


def part2(data: str) -> int:
    invalids = 0
    ranges = data.split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        invalids += count_invalids_more_than_twice(start, end)
    return invalids


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_input(str(input_file))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
