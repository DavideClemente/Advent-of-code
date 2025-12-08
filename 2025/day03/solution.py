"""
Advent of Code - Day 03
https://adventofcode.com/2025/day/3
"""

from common import read_input, read_lines
from pathlib import Path
from itertools import combinations
import sys

# Add common utilities to path
sys.path.append(str(Path(__file__).parent.parent))

class BatteryBank:
    def __init__(self, battery_joltage_ratings):
        self.battery_joltage_ratings = battery_joltage_ratings
    
    def get_largest_joltage_possible(self, batteries):
        """Find largest number by concatenating 'batteries' count of ratings."""
        joltage_output = []
        
        idx = -1
        for i in range(batteries - 1, -1, -1):
            idx = self._find_index_of_highest_digit(
                idx + 1, 
                len(self.battery_joltage_ratings) - i
            )
            joltage_output.append(str(self.battery_joltage_ratings[idx]))
        
        return int(''.join(joltage_output))
    
    def _find_index_of_highest_digit(self, start, end):
        """Find index of highest rating in range [start, end)."""
        highest_digit = 0
        idx = -1
        
        for i in range(start, end):
            rating = self.battery_joltage_ratings[i]
            if int(rating) > highest_digit:
                highest_digit = int(rating)
                idx = i
        
        return idx


def part1(batteries: list[BatteryBank]) -> int:
    """Solve part 1 of the puzzle."""
    # TODO: Implement solution
    return sum(b.get_largest_joltage_possible(2) for b in batteries)


def part2(batteries: list[BatteryBank]) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    return sum(b.get_largest_joltage_possible(12) for b in batteries)


def main():
    # Read input
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))
    
    data = list(map(lambda e: BatteryBank(e), data))

    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
