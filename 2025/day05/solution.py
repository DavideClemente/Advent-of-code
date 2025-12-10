"""
Advent of Code - Day 05
https://adventofcode.com/2025/day/5
"""

from common import read_input, read_lines, Range
from pathlib import Path
from py_linq.py_linq import Enumerable
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))

def is_ingredient_fresh(ranges: list[Range], ingredient: int) -> bool:
    return Enumerable(ranges).any(lambda x: ingredient in x)


def part1(ranges: list[Range], ingredients: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    return Enumerable(ingredients).where(lambda x: is_ingredient_fresh(ranges, int(x))).count()
    


def part2_2(ranges: list[Range]) -> int:
    intervals = [tuple(map(int, r.split('-'))) for r in ranges]
    intervals.sort()

    merged = []
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_end + 1:          # overlap or touching
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))

    # count unique IDs
    return sum(e - s + 1 for s, e in merged)



def part2(ranges: list[Range]) -> int:
    ranges.sort()

    return 0

def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))
    idx = data.index('')
    ranges, ingredients = data[:idx], data[idx+1:]
    ranges = [Range(*map(int, r.split('-'))) for r in ranges]

    # Solve and print results
    print(f"Part 1: {part1(ranges, ingredients)}")
    print(f"Part 2: {part2(ranges)}")


if __name__ == "__main__":
    main()
